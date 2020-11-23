#
# VPNDetectorBulk v1.4
#
# This script should be used primarly for
# bulk lookups from files of IP addresses
#
# Coded by IlluminatiFish
#

from bs4 import BeautifulSoup
import requests, re

spans = []

def cleanHTML(raw_html):
  cleaner = re.compile('<.*?>')
  cleantext = re.sub(cleaner, '', str(raw_html))
  return cleantext.strip()

def clearParagraph(raw_paragraph):
    return str(raw_paragraph).split('is part of ')[1].split('.')[0]

def getProvider(ip):
    spans.clear()
    
    r = requests.get('https://spur.us/context/{}'.format(ip))
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    for span in soup.find_all('span'):
        spans.append(span)

    if len(spans) > 2:
        
        if cleanHTML(spans[2]) == "Not Anonymous" or cleanHTML(spans[2]) == "Possibly Anonymous" or cleanHTML(spans[2]) == "Likely Anonymous":
            return None

        if cleanHTML(spans[2]) == '': #Catches Proxies
            paras = soup.find_all('p')
            return clearParagraph(paras[0]).upper() 
       
        return cleanHTML(spans[2]).upper()

f = open('ips.txt', 'r')

correct = 0
total = 0

for x in f.readlines():
    total += 1
    
    if getProvider(x.strip()) is not None:
        print('Provider:',getProvider(x.strip()), '~~~ IP:',x.strip())
        correct += 1

print("Results: {}/{}".format(correct, total))

  
    
