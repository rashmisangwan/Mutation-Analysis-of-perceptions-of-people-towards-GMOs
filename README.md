1. Install libraries `pip install pandas tweepy indicoio`

2. In terminal move to this repo's directory and run

    > This fetches the tweets related to the array of words mentioned in line 35 of fetch.py

    > file named 'twitter_data.txt' will be created

    > #### python fetch.py


3. In terminal in current directory run

    > file named 'twitter_data.json' and 'twitter_data.csv' will be created

    > This parses the twitter_data.txt to JSON data and -

        - save it in twitter_data.json file

        - save the selected fields data in twitter_data.csv file (that can be opened in msexcel for preview)

            - line 26 acts as the header for the selected fields for the CSV file

            - line 32-40 acts as the Content for the selected fields for the CSV file

        - Analyse and adds the sentiment score for each tweet.

    > #### python parse.py

4. Parse the csv files using various parsers - like for language, location and time of days, etc. These will create an aggregated table that can be used for charts generation. Run `python parse-*.py` with * as chosen parser.

5. Remove junks like - retweets, unknown, etc. Run `python remove-*.py`with * as chosen parser.

5. Open the CSV file in msexcel or any other software or online that supports CSV

6. Run fetch command any number of times. This will only append to the existing set of data.


TODO: Will share the research paper and report after it's final publishing on IEEE
