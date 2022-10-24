pipeline {
    agent {label 'Ansible-CN-40'}

  environment {
      VAULT_PASS_FILE = credentials('Ansible_Vault_File')
      URL_DOMAIN_VAR = "github.com"
      DNS_SERVER_VAR = credentials('Beijing_DNS')
      TODAY_DATE_VAR = sh(returnStdout: true, script: 'date +%Y%m%d').trim()
      RECORD_FILE_PATH = "/home/jenkins/Ansible/dns_resolving_records/dns-resolved-${URL_DOMAIN_VAR}-${TODAY_DATE_VAR}.txt"
  }
    
    stages {
        stage('DNS_Resolving') {
            steps {
                sh '''
                /home/jenkins/Ansible/ansible/bin/python3 /home/jenkins/jenkins-with-ansible/dns_resolv.py ${DNS_SERVER_VAR} ${URL_DOMAIN_VAR}
                /usr/bin/cp /home/jenkins/Ansible/roles/firewall_cisco/tasks/main.yml /home/jenkins/Ansible/roles/firewall_cisco/tasks/main.backup
                '''
            }
        }
        
        stage('Playbook manipulation') {
              steps {
                sh '''
                  for i in $(cat ${RECORD_FILE_PATH}); do /usr/bin/sed -i \
                  "s/lines:/lines:\\n      - access-list {{ dehong_asa_acl_ctas }} extended permit ip object-group DehongStaffNetwork host $i/g" \
                  /home/jenkins/Ansible/roles/firewall_cisco/tasks/main.yml; done
                 '''
                }
              }

        stage('Run Ansible playbook') {
              steps {
                sh '''
                  source /home/jenkins/Ansible/ansible/bin/activate
                  /home/jenkins/.local/bin/ansible-playbook -i /home/jenkins/Ansible/hosts.ini /home/jenkins/Ansible/playbook.yml --vault-password-file ${VAULT_PASS_FILE}
                  /usr/bin/mv /home/jenkins/Ansible/roles/firewall_cisco/tasks/main.backup /home/jenkins/Ansible/roles/firewall_cisco/tasks/main.yml
                 '''
                }
           }
     }
}
