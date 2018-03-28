# Import all required libraries
import json

# Tweepy library - realtime tweets streaming library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# User credentials to access Twitter API
access_token =              "###############################"
access_token_secret =       "###############################"
consumer_key =              "###############################"
consumer_secret =           "###############################"

# Fetched raw tweets data is saved in `twitter_data.txt`
fileObject = open('twitter_data.txt', 'a')

# Counter for the number of tweets fetched
tweets_fetch_counter = 0

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        global tweets_fetch_counter
        tweets_fetch_counter = tweets_fetch_counter + 1

        print('Fetched tweet number # ', json.dumps(tweets_fetch_counter))

        fileObject.write(data)
        return True

    def on_error(self, status):
        print('x x x x x x x x x x x x x x x x x x x x x x x x x x x x ')
        print('Fetch error - ', status)
        print('x x x x x x x x x x x x x x x x x x x x x x x x x x x x ')

# This is the main tweets fetcher - captures tweets from streaming API based on keywords
def runFetcher():
    try:
        # This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)

        # This line filter Twitter Streams to capture data by the keywords: 
        #   - Takes an array of keywords to filter the related tweets
        stream.filter(track=['genetic modified organisms', 'genetically modified crops', 'genetic modified organism', 'gmo', 'genetic modified', 'genetically modified', 'genetic engineering', 'agriculture biotechnology', 'gene expression', 'transgene', 'genetic manipulation', 'golden rice project', 'transgenic plants', 'golden rice'])
    except:
        print('- - - - - - - - - - - - - Retrying again after exception - - - - - - - - - - - - - -')
        runFetcher()

# Run Fetcher only if this file is interpreted directly
if (__name__ == '__main__'):
    runFetcher()
