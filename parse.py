# Import all required libraries

import json
import csv
import pandas as pd

# Sentiment Analysis API
import indicoio

def main():
    ''' 
        Initialise the required data and files 
    '''

    # Open the data files
    tweets_file = open('./twitter_data.txt', 'r')               # Fetched tweets by Tweepy are in here
    tweets_json_file = open('./twitter_data.json', 'a')         # Fetched tweets are put here after refining the jSON
    tweets_csv_file = open('./twitter_data.csv', 'a')           # Fetched tweets are put here with selected keys in CSV format

    # Make the file CSV ready
    csvwriter = csv.writer(tweets_csv_file)

    # Init data variables
    indicoio.config.api_key = '################################' # Indicoio API key for sentiment score API
    headerSet = False                                            # Flag for setting the header row

    tweets_json_file.write('[')                                  # Data fetched is JSON data array without the enclosing '[' bracket, hence needs to be mannually inserted

    # Loop over the fetched tweep fron the the tweeps_file
    for unparsedTweet in tweets_file:
        if not unparsedTweet:
            continue

        try:
            tweet = json.loads(unparsedTweet)
            tweets_json_file.write(json.dumps(tweet))
            tweets_json_file.write(',')

            # Write header row for CSV file
            if ( not headerSet ):
                csvwriter.writerow(['username', 'location', 'sentiment', 'sentiment-score', 'text', 'time_zone', 'created_at', 'place', 'lang', 'quote_count', 'reply_count', 'retweeted', 'retweet_count', 'favorited', 'favorite_count', 'timestamp_ms', 'followers_count', 'friends_count', 'statuses_count'])
                headerSet = True

            # Compute sentiment score using the Indicoio Library
            sentimentScore  = indicoio.sentiment_hq(tweet['text'])
            sentiment       =   'NEUTRAL'
            if sentimentScore < .4:
                sentiment   = 'NEGATIVE'
            elif sentimentScore > .6:
                sentiment   = 'POSITIVE'

            tweet["sentiment_score"] = sentimentScore
            tweet["sentiment"] = sentiment

            # Make csv writable data ready
            data = []
            data.append(tweet['user']['name'])
            data.append(tweet['user']['location'])
            data.append(tweet["sentiment"])
            data.append(tweet["sentiment_score"])
            data.append(tweet['text'])
            data.append(tweet['user']['time_zone'])
            data.append(tweet['created_at'])
            data.append(tweet['place'])
            data.append(tweet['lang'])
            data.append(tweet['quote_count'])
            data.append(tweet['reply_count'])
            data.append(tweet['retweeted'])
            data.append(tweet['retweet_count'])
            data.append(tweet['favorited'])
            data.append(tweet['favorite_count'])
            data.append(tweet['timestamp_ms'])
            data.append(tweet['user']['followers_count'])
            data.append(tweet['user']['friends_count'])
            data.append(tweet['user']['statuses_count'])

            print(data)

            csvwriter.writerow(data)
        except:
            continue

    tweets_json_file.write(']')

# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()