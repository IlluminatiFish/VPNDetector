from bs4 import BeautifulSoup
import requests, re

def get_vpn_provider(ip):
  
    request = requests.get('https://spur.us/context/{}'.format(ip))
    soup = BeautifulSoup(request.text, 'html.parser')
    
    for meta_tag in soup.find_all('meta'):
        search = re.search('(.*) \( (.*) \) IP Context', str(meta_tag.get('content')))
        if search:
            return search.group(2)


ip = input("[+] IP: ")
result = get_vpn_provider(ip)
print('Provider:', result)



  
    


  
    
