import requests
from bs4 import BeautifulSoup
def putcontent(url):
			r=requests.get(url);
			soup=BeautifulSoup(r.content)
			word=getatt.find(url)
			g_data=soup.find_all(word[1],{word[2]:word[3]})
			s="";
			for item in g_data:
				s+=item.text
			print(s);
