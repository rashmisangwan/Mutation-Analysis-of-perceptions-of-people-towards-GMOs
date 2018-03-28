1. Install panda for python in windows

2. Install tweepy for python in windows

3. In terminal move to the current directory and run


    > # This fetches the tweets related to the array of words mentioned in line 35 of fetch.py

    > # file named 'twitter_data.txt' will be created

    > python fetch.py > twitter_data.txt


4. In terminal in current directory run


    > # file named 'twitter_data.json' and 'twitter_data.csv' will be created

    > # This parses the twitter_data.txt to JSON data and -

        - save it in twitter_data.json file

        - save the selected fields data in twitter_data.csv file (that can be opened in msexcel for preview)

            - line 26 acts as the header for the selected fields for the CSV file

            - line 32-40 acts as the Content for the selected fields for the CSV file

        - Prints the selected data to terminal (Command Prompt)

    > python parse.py


5. Open the CSV file in msexcel or any other software or online that supports CSV

6. Run fetch command any number of times. This will only append to the existing set of data.
