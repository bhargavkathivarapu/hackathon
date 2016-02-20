import feedparser

feed = feedparser.parse("http://www.thehindu.com/news/cities/Hyderabad/?service=rss")
date=time.strftime("%d %b %Y");
for item in feed["items"]:
	if date in item["published"].encode('ascii','ignore'):
		s=item["published"].encode('ascii','ignore')
		print(s)
		#f.write(s)
		print item["title"]
		#f.write(item["title"])
		print item["description"]
		#f.write(item["description"])
		#f.write("-|")
		print
		print
