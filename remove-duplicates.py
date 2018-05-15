# Import all required libraries

import json
import csv
import re

def main():
    '''
        Removes all the duplicates from the collected data
    '''

    # Open the data files
    sentiment_file          = open('./twitter_data.csv', 'r')
    removed_duplicates_file   = open('./twitter_data-duplicates-removed.csv', 'w')
    duplicates_file           = open('./twitter_data-duplicates.csv', 'w')

    # Make the file CSV ready
    reader_parsed_data   = csv.reader(sentiment_file)
    writer_no_duplicates   = csv.writer(removed_duplicates_file)
    writer_only_duplicates = csv.writer(duplicates_file)

    reader_parsed_data = sorted(reader_parsed_data, key=lambda row: row[15], reverse=True)
    
    prev_row = ''
    for row in reader_parsed_data:
        if prev_row and prev_row[15] == row[15] and prev_row[4] == row[4] :
            writer_only_duplicates.writerow(row)
        else:
            writer_no_duplicates.writerow(row)
        
        prev_row = row

    sentiment_file.close()
    removed_duplicates_file.close()
    duplicates_file.close()



# Run Parser only if this file is interpreted directly
if (__name__ == '__main__'):
    main()