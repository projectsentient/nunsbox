import requests

def VETR():
	print "Connecting to VETR..."
	
	VETR_key = "zevrUyoCP6JM9r9AA4DkBW8LRbAV2r1Z"
	ticker = "NASDAQ:AAPL"
	start = 0
	limit = 100
		
	params = {
		"ticker" : ticker,
		"apikey" : VETR_key}
		
	#Initial pull -> company profile 	
	j1 = requests.get("https://vetr-prod.apigee.net/v1/api/research/securityInfo?", params=params).json()
	#code placed here to store company data into database
	
	#Second pull -> Loop to pull all posts given the ticker starting from index 0:
	while True:
		str_start = str(start)
		str_limit = str(limit)
		params = {
			"ticker" : ticker,
			"sortBy" : "created_on:asc",
			"fullText" : "true",
			"start" : str_start,
			"limit" : str_limit,
			"apikey" : VETR_key}
			
		j = requests.get("https://vetr-prod.apigee.net/v1/api/posts/ticker?", params=params).json()
		#code here to loop through and place each post into database
		start = start + 100
		limit = limit + 100
		
VETR()