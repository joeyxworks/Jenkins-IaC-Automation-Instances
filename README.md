# Jenkins-IaC-Automation-Instances
Jenkins IaC Automation Instances, this repo shows instances that using Ansible playbook to push configuration updates to Cisco ASA firewall.

# Content
- Jenkins Pipeline
- Ansible Playbook
- Python Script

# Jenkins Pipeline
> Because Java is the key component for Jenkins, make sure you install the same version between controll node and agent node
> here's using openjdk 11.0.16 2022-07-19 LTS
Instatnce pipeline is divided into four parts, the first is to define the required variables which will be used in the following parts. The second part runs python script *dns_resolv.py* and write down the resolved A records into txt file. The third part use a for loop with values in previous records file and then replace lines in the roles tasks file with sed. Final part is to run the playbook with ansible.

# Ansible Playbook
> Ansible components used here are **cisco.asa** and **paramiko**
Playbook file uses roles to simplify the structure of a single playbook. In the configuration deployment, Ansible's **cisco.asa** module is used to apply linear configuration to target device.

# Python Script
This script aims to resolve the DNS record and then save the IP resolved into file.