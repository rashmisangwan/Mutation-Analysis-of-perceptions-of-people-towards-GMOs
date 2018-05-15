import json
import csv

def main():
    ''' 
        Initialise the required data and files 
    '''

    headerSet = False

    # Open the data files
    tweets_csv_file = open('./twitter_data-unknown.csv', 'r')
    tweets_csv_updated_file = open('./twitter_data-unknown_bubble.csv', 'w')

    # Make the file CSV ready)
    csvreader = csv.reader(tweets_csv_file, delimiter=',')
    csvwriter = csv.writer(tweets_csv_updated_file)

    # counter = 0
    returnObj = {}
    
    for row in csvreader:
        key = row[8]
        if not (key in returnObj.keys()):
            returnObj[key] = []
        
        returnObj[key].append(row)

    headItem = ['lang', 'tweets_count', 'sentiment_score', 'followers_count']
    # csvwriter.writerow(headItem)
    for key in returnObj.keys():
        returnItem = ['',0,0,0]
        count = int(len(returnObj[key]))
        for item in returnObj[key]:
            returnItem[0] = item[8]
            returnItem[1] = returnItem[1] + 1
            returnItem[2] = returnItem[2] + float(item[3])
            returnItem[3] = returnItem[3] + int(item[16])
            count = count + 1

        returnItem[0] = item[8]
        returnItem[1] = returnItem[1]
        returnItem[2] = returnItem[2] / count
        returnItem[3] = int(returnItem[3] / count)
        # csvwriter.writerow(returnItem)
    

main()