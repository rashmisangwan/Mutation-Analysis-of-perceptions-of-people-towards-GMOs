# Import all required libraries

import json
import csv
import re

def main():
    '''
        Removes all the unknown lang from the collected data
    '''

    # Open the data files
    sentiment_file          = open('./twitter_data.csv', 'r')
    removed_unknown_file   = open('./twitter_data-unknown-removed.csv', 'w')
    unknown_file           = open('./twitter_data-unknown.csv', 'w')

    # Make the file CSV ready
    reader_parsed_data   = csv.reader(sentiment_file)
    writer_no_unknown   = csv.writer(removed_unknown_file)
    writer_only_unknown = csv.writer(unknown_file)

    pattern = re.compile('und')

    for row in reader_parsed_data:
        if pattern.match(row[8]):
            writer_only_unknown.writerow(row)
        else:
            writer_no_unknown.writerow(row)

    sentiment_file.close()
    removed_unknown_file.close()
    unknown_file.close()



# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()