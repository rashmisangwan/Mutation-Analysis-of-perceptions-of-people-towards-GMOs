# Import all required libraries

import json
import csv
import re

def main():
    '''
        Removes all the junk from the collected data
    '''

    # Open the data files
    sentiment_file      = open('./twitter_data.csv', 'r')
    pure_data           = open('./twitter_data-pure.csv', 'w')
    junk_data           = open('./twitter_data-junk.csv', 'w')

    # Make the file CSV ready
    reader_parsed_data  = csv.reader(sentiment_file)
    writer_pure_data    = csv.writer(pure_data)
    writer_only_junk    = csv.writer(junk_data)

    # patternReplies  = re.compile('(@)+')
    patternRetweets = re.compile('(RT @)+')
    patternUnknown  = re.compile('und')

    reader_parsed_data = sorted(reader_parsed_data, key=lambda row: row[15], reverse=True)
    prev_row = ''

    for row in reader_parsed_data:
        if prev_row and prev_row[15] == row[15] and prev_row[4] == row[4] :
            writer_only_junk.writerow(row)
        elif patternRetweets.match(row[4]) or patternUnknown.match(row[8]):
            writer_only_junk.writerow(row)
        else:
            writer_pure_data.writerow(row)
        
        prev_row = row

    sentiment_file.close()
    pure_data.close()
    junk_data.close()



# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()