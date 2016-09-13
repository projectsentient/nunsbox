import requests

def StockTwits():
	print "Connecting to StockTwits..."
	
	ticker = "AAPL"
	
	while True:
		params = {
			"id" : ticker,
			"since" : id,
			"limit" : "30"}

		j = requests.get("https://api.stocktwits.com/api/2/streams/symbol/AAPL.json?", params=params).json()
		#code here to save JSON data to database
StockTwits()