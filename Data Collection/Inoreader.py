import requests

def InoReader():
	
	print "Connecting to Inoreader..."

	parameters = {
		"Email" : "williamdelmontlupo@gmail.com",
		"Passwd" : "lupo1989"}
	#client login api -> grabs the authentication token and saves to Auth
	reponse = requests.post("https://www.inoreader.com/accounts/ClientLogin", params=parameters)
	r = (reponse.content)
	A = r[24:]
	Auth = str(A).rstrip()
	
	headers = {
		"User-Agent" : "Sentiment Algorithm",
		"Host" : "www.inoreader.com",
		"Authorization" : "GoogleLogin auth="+ Auth,
		"AppId" : "1000000951",
		"AppKey": "eSPe0xmBdGEamNrCU3QN7qyPkf9OiDCB"}
	params = {
		"n" : "1",
		"": "user/-/label/Business"}
		
	response = requests.post("https://www.inoreader.com/reader/api/0/stream/contents/", headers=headers, params=params)
	js = response.json()

	cont = js["continuation"]
	url = js["items"][0]["canonical"][0]["href"]
	
	cont_str = str(cont)
	print "Extacting RSS Article..."

	articles = []
	articles.append(url)
	articles_pulled = 1
	while (articles_pulled <= 50000):		
		params = {
			"n" : "1",
			"includeAllDirectStreamIds" : "true",
			"c" : cont_str,
			"" : "user/-/label/Business"}
			
		js = requests.post("https://www.inoreader.com/reader/api/0/stream/contents/", headers=headers, params=params).json()
		
		cont = js["continuation"]
		url = js["items"][0]["canonical"][0]["href"]
		cont_str = str(cont)
		articles_pulled = articles_pulled + 1
		if url not in articles:
			articles.append(url)
		continue
	return articles
InoReader()