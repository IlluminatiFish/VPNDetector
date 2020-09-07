#
# VPNDetector
#
# This script should be used primarly for
# singular IP lookups 
#
# Coded by IlluminatiFish
#

from bs4 import BeautifulSoup
import requests, re

def cleanHTML(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', str(raw_html))
  return cleantext.strip()


spans = []
def getProvider(ip):
    spans.clear()
    r = requests.get('https://spur.us/context/{}'.format(ip))
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in soup.find_all('span'):
        spans.append(i)
    if len(spans) > 1:
        if cleanHTML(spans[1]) == "Not Anonymous" or cleanHTML(spans[1]) == "Possibly Anonymous":
            return None
        return cleanHTML(spans[1])

raw_ip = input("[+] IP: ")

print("IP:",raw_ip)
print("Provider:",getProvider(raw_ip).replace(" ", "")+ "VPN")


  
    
