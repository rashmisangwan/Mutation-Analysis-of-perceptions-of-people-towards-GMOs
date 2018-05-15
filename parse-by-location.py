import json
import csv
from pytz import country_timezones
import math

def main():
    ''' 
        Initialise the required data and files 
    '''

    headerSet = False

    # Open the data files
    tweets_csv_file = open('./twitter_data.csv', 'r')
    tweets_csv_updated_file = open('./twitter_data-location_bubble.csv', 'w')

    # Make the file CSV ready)
    csvreader = csv.reader(tweets_csv_file, delimiter=',')
    csvwriter = csv.writer(tweets_csv_updated_file)

    returnObj = {}

    timezone_countries = {}
    for country, timezones in country_timezones.items():
        for timezone in timezones:
            timezone_countries.setdefault(timezone, set()).add(country)
    
    for row in csvreader:
        if not headerSet or row[5] == 'time_zone':
            headerSet = True
        else:
            if not row[5] or not row[8]:
                key = 'unknown'
            else:
                key = row[5]
            if not (key in returnObj.keys()):
                returnObj[key] = []
            
            returnObj[key].append(row)

    headItem = ['time zone', 'popularity (tweets count)', 'sentiment score', 'followers count', 'country']
    csvwriter.writerow(headItem)
    for key in returnObj.keys():
        returnItem = ['',0,0,0, []]
        count = int(len(returnObj[key]))

        returnItem[0] = key
        returnItem[1] = count
        for item in returnObj[key]:
            returnItem[2] = returnItem[2] + float(item[3])
            returnItem[3] = returnItem[3] + int(item[16])

        returnItem[2] = math.log(returnItem[2] / count)
        returnItem[3] = math.log(int(returnItem[3] / count))
        if key in timezone_countries.keys():
            returnItem[4] += timezone_countries[key]
        else:
            returnItem[4] += ['unknown']

        csvwriter.writerow(returnItem)

main()