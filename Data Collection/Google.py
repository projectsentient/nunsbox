import requests

def GoogleSearch():
	API_key = "AIzaSyD85dyT7oeSZd-V9FBAVmMTtSFn8E9Zpnk"

	print "Connecting to Google Search..."

	start = 1	
	while True:	
		str_start = str(start)
		params = {
			"q" : "AAPL News",
			"cx" : "012478775954940262604:yexwef2fhs8",
			"filter" : "1",
			"start" : str_start,
			"key" : API_key}
		try:
			j = requests.get("https://www.googleapis.com/customsearch/v1?", params=params).json()
			
			start = start + 10
			articles = []
			num = 0
			while True:
				url = j["items"][num]["link"]		
				if url not in articles:
					articles.append(url)
				num = num + 1
				if (num > 9) : break
		except: 
			print articles
			print "Max Links Pulled."
			break
GoogleSearch()