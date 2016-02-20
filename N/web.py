from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import requests
from bs4 import BeautifulSoup
import getatt


alchemyapi = AlchemyAPI()
keys=["elon musk","tesla"]
url="http://techcrunch.com/2016/01/29/tesla-says-ceo-elon-musk-just-bought-more-of-the-company/"
r=requests.get(url);
soup=BeautifulSoup(r.content)
word=getatt.find(url)
g_data=soup.find_all(word[1],{word[2]:word[3]})
s="";
for item in g_data:
	s+=item.text

print(s);

"""
flag=0;
for i in range(0,len(keys)):
	if( keys[i] in s.lower()):
		flag=1;


if flag==1:

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
else:
	print("NOT RELAVENT TO GIVEN KEYS")
"""
