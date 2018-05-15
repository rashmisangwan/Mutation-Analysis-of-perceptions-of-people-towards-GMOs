# Import all required libraries

import json
import csv
import re

def main():
    '''
        Removes all the retweets from the collected data
    '''

    # Open the data files
    sentiment_file          = open('./twitter_data.csv', 'r')
    removed_retweets_file   = open('./twitter_data-rt-removed.csv', 'w')
    retweets_file           = open('./twitter_data-rt.csv', 'w')

    # Make the file CSV ready
    reader_parsed_data   = csv.reader(sentiment_file)
    writer_no_retweets   = csv.writer(removed_retweets_file)
    writer_only_retweets = csv.writer(retweets_file)

    pattern = re.compile('(RT @)+', re.I)

    for row in reader_parsed_data:
        if pattern.match(row[4]):
            writer_only_retweets.writerow(row)
        else:
            writer_no_retweets.writerow(row)

    sentiment_file.close()
    removed_retweets_file.close()
    retweets_file.close()



# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()