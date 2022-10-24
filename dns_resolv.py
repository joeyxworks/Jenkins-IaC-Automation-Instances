#!/home/jenkins/Ansible/ansible python
from datetime import date
import sys
import dns.resolver

# Store today's date into variable
today = date.today().strftime("%Y%m%d")

# Module instancing
resolver = dns.resolver.Resolver()
resolver.lifetime= 1
resolver.timeout= 0.5

# Store the first arg and second arg into variables
DNS_SERVER = sys.argv[1]
DOMAIN_URL = sys.argv[2]

# Define function for storing results resolved by dnspython into file.
def getARecord(dnsServer, domainName):
    resolver.nameservers = [dnsServer]
    answers = resolver.resolve(domainName, 'A')
    result_list = []
    with open('/home/jenkins/Ansible/dns_resolving_records/dns-resolved-{}-{}.txt'.format(domainName, today), 'w')  as f:
        for answer in answers:
#            result_list.append(str(answer))
            print('[*] {} has IP'.format(domainName), answer, 'resolved.')
            f.write("{}\n".format(str(answer)))
        f.close()
#    return result_list

if __name__ == '__main__':
    getARecord(DNS_SERVER, DOMAIN_URL)