# Import all required libraries

import json
import csv
import re

def main():
    '''
        Removes all the replies from the collected data
    '''

    # Open the data files
    sentiment_file         = open('./twitter_data.csv', 'r')
    removed_replies_file   = open('./twitter_data-replies-removed.csv', 'w')
    replies_file           = open('./twitter_data-replies.csv', 'w')

    # Make the file CSV ready
    reader_parsed_data   = csv.reader(sentiment_file)
    writer_no_replies    = csv.writer(removed_replies_file)
    writer_only_replies  = csv.writer(replies_file)

    pattern = re.compile('(@)+', re.I)

    for row in reader_parsed_data:
        if pattern.match(row[4]):
            writer_only_replies.writerow(row)
        else:
            writer_no_replies.writerow(row)

    sentiment_file.close()
    removed_replies_file.close()
    replies_file.close()



# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()