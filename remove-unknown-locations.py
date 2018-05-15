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
    removed_unknown_locations_file   = open('./twitter_data-unknwon-location-removed.csv', 'w')
    unknown_location_file           = open('./twitter_data-unknwon-location.csv', 'w')

    # Make the file CSV ready
    reader_parsed_data   = csv.reader(sentiment_file)
    writer_no_unknown_locations   = csv.writer(removed_unknown_locations_file)
    writer_only_unknown_locations = csv.writer(unknown_location_file)

    for row in reader_parsed_data:
        if not row[5] or not row[8]:
            writer_only_unknown_locations.writerow(row)
        else:
            writer_no_unknown_locations.writerow(row)

    sentiment_file.close()
    removed_unknown_locations_file.close()
    unknown_location_file.close()



# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()