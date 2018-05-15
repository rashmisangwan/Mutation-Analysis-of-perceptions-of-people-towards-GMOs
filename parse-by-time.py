import json
import csv
import random
import time
from datetime import datetime
from dateutil.parser import parse
import math

def main():
    ''' 
        Initialise the required data and files 
    '''

    headerSet = False

    # Open the data files
    tweets_csv_file = open('./twitter_data.csv', 'r')
    tweets_csv_new_file = open('./twitter_data_new.csv', 'w')
    tweets_csv_updated_file = open('./twitter_data-time_bubble.csv', 'w')

    # Make the file CSV ready)
    csvreader = csv.reader(tweets_csv_file, delimiter=',')
    csvNewwriter = csv.writer(tweets_csv_new_file)
    csvwriter = csv.writer(tweets_csv_updated_file)

    returnObj = {}

    for row in csvreader:
        if not headerSet or row[6] == 'created_at':
            headerSet = True
            csvNewwriter.writerow(row)
        else:
            if not row[5] or not row[6] or not row[8]:
                key = 'unknown'
                csvNewwriter.writerow(row)
            else:
                time_struct = time.strptime(row[6], "%a %b %d %H:%M:%S +0000 %Y")
                date_struct = datetime.fromtimestamp(time.mktime(time_struct))

                row_split = row[6].split(' ')
                time_split = row_split[3].split(':')
                time_split[0] = random.randint(0,23)
                if time_split[0] < 10:
                    time_split[0] = '0' + str(time_split[0])
                else:
                    time_split[0] = str(time_split[0])
                    
                row_split[3] = ':'.join(time_split)
                row_split = ' '.join(row_split)

                if date_struct.hour < 12:
                    key = 'morning'
                elif 12 <= date_struct.hour < 18:
                    key = 'afternoon'
                else:
                    key = 'evening'
                csvNewwriter.writerow(row)

            if not (key in returnObj.keys()):
                returnObj[key] = []
            
            returnObj[key].append(row)

    headItem = ['time of tweet', 'popularity (tweets count)', 'sentiment score', 'followers count']
    csvwriter.writerow(headItem)
    for key in returnObj.keys():
        returnItem = ['',0,0,0]
        count = int(len(returnObj[key]))

        returnItem[0] = key
        returnItem[1] = count
        for item in returnObj[key]:
            returnItem[2] = returnItem[2] + float(item[3])
            returnItem[3] = returnItem[3] + int(item[16])
            if( float(item[3]) < 0 ):
                print(item)

        returnItem[2] = returnItem[2] / count
        returnItem[3] = int(returnItem[3] / count)

        csvwriter.writerow(returnItem)

main()