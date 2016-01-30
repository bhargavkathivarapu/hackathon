from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import requests
from bs4 import BeautifulSoup



alchemyapi = AlchemyAPI()
url="http://social.yourstory.com/2013/09/how-nit-warangal-lakshya-foundation-bridged-gap-alumni-and-students/"
r=requests.get(url);
soup=BeautifulSoup(r.content)

g_data=soup.find_all("div",{"class":"ys_post_content text"})
s="";
for item in g_data:
	s+=item.text
	
response = alchemyapi.keywords('text',s, {'sentiment':1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])
