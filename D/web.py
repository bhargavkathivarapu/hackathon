import requests
from bs4 import BeautifulSoup
from DatumBox import DatumBox
API_KEY = "2a13913dda346761765020c1f66e34f8"

datum_box = DatumBox(API_KEY)
url="http://social.yourstory.com/2013/09/how-nit-warangal-lakshya-foundation-bridged-gap-alumni-and-students/"
r=requests.get(url);
soup=BeautifulSoup(r.content)

g_data=soup.find_all("div",{"class":"ys_post_content text"})

s=""
for item in g_data:
	s+=item.text

print s
x= datum_box.keyword_extract(s.encode('ascii','ignore'))
keys=["NIT","RECW","WARANGAL"]
for i in x:
	print i.encode('ascii','ignore') 
	if i.encode('ascii','ignore').upper() in keys:
		print i.encode('ascii','ignore')
		


