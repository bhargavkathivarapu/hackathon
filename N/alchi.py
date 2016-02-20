from __future__ import print_function
from alchemyapi import AlchemyAPI
import json


keys=["elon musk","tesla"]

inp=open('feeds.db','r');
des=""
for line in inp:
	if "-|" not in line:
		des+=line;
	else:
		print(des)
	
		flag=0;
		for i in range(0,len(keys)):
			if( keys[i] in des.lower()):
				flag=1;


		if flag==1:
			alchemyapi = AlchemyAPI()
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
		print
		des=""
	

