import re

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