import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from textblob import TextBlob
from textblob import Blobber
# from textblob.sentiments import NaiveBayesAnalyzer

# self.sentiment_analyzer = SentimentIntensityAnalyzer()
# self.blobber = Blobber(analyzer=NaiveBayesAnalyzer())
# print("training...")
# analysis = self.blobber("training take a long time doesn't it!")
# analysis.sentiment
# print("trained!")

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    # create TextBlob object of passed tweet text
    cleaned_tweet = clean_tweet(tweet)
    analysis = TextBlob(cleaned_tweet)
    return analysis.sentiment.polarity

    # analysis = self.blobber(self.__clean_tweet(tweet))
    # if analysis.sentiment.classification == 'pos' and analysis.sentiment.p_pos == 0.5:
    #     return 0.0
    # elif analysis.sentiment.classification == 'neg':
    #     return -analysis.sentiment.p_neg
    # else:
    #     return analysis.sentiment.p_pos

    # cleaned_tweet = clean_tweet(tweet)
    # vs = SentimentIntensityAnalyzer().polarity_scores(cleaned_tweet)
    # return vs['compound']