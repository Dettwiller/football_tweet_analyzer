import re
import os
from datetime import datetime, timedelta

import tools
from textblob import TextBlob
from textblob import Blobber

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    # create TextBlob object of passed tweet text
    cleaned_tweet = clean_tweet(tweet)
    analysis = TextBlob(cleaned_tweet)
    return analysis.sentiment.polarity

def get_last_analyzed_file(analyzed_data_path):
    start_date = datetime(2019, 8, 2)
    today = datetime.now()
    while today >= start_date:
        candidate_filename = "{:%Y-%B-%d}".format(today) + ".csv"
        if os.path.exists(os.path.join(analyzed_data_path, candidate_filename)):
            return today
        else:
            today -= timedelta(days=1)
    return start_date

def analyze_raw_files(raw_data_path, analyzed_data_path):
    start_date = get_last_analyzed_file(analyzed_data_path)
    today = datetime.now()
    tweet_files = tools.get_dated_files(raw_data_path, today, start_date)
    for tweet_file in tweet_files:
        with open(os.path.join(raw_data_path, tweet_file), "r", encoding="utf-8", errors='ignore') as rtf:
            with open(os.path.join(analyzed_data_path, tweet_file), "w+", encoding='utf-8', errors='ignore') as atf:
                line = rtf.readline() # user, content, hashtags, date
                while line:
                    list_line = line.strip().split(",")
                    if len(list_line) == 4:
                        tweet_sentiment = get_tweet_sentiment(list_line[1])
                        output_list_line = [list_line[1], list_line[2], str(tweet_sentiment), list_line[3]]
                        # content, hashtags, sentiment, date
                        atf.write(",".join(output_list_line) + "\n")
                    line = rtf.readline()