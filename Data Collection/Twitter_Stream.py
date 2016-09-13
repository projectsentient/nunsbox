from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

conn = sqlite3.connect("Twitter_Stream.sqlite")
cur = conn.cursor()

#consumer key, consumer secret, access token, access secret.
ckey="SVDCo1YtzjifMwczc0N8chhSB"
csecret="90S7xg7UXRe0DD3CVrNd0xsv5qsUA26cdyZkbtYOuP9Z0oqK1X"
atoken="279419107-tUPhlZAmcQ2rB1wbWruHahdu8eSgoblGX4cKFH6L"
asecret='xIusl6ovNfwccsVJJm9MUc6aVZu1IQtTy3LlhI1pbzxuA'

class listener(StreamListener):

    def on_data(self, data):
		js = json.loads(data)
		date = js["created_at"]
		handle = js["user"]["screen_name"]
		text = js["text"]
		print "Extracting Tweet...."
		return(True)

    def on_error(self, status):
		print status
		
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["$AAPL"])