import os
import time
from datetime import datetime
import tweepy


class TwitterAccount():
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        # TODO type check those strings
        # self.consumer_key = consumer_key
        # self.consumer_secret = consumer_secret
        # self.access_token = access_token
        # self.access_token_secret = access_token_secret

        try:
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit = True)
        except:
            raise ValueError("provided keys did not authenticate")

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, twitter_account_object, data_path):
        # tweepy.StreamListener.__init__(self)
        super().__init__()
        self.twitter_object = twitter_account_object
        self.raw_data_path = data_path + os.sep + "raw"

    def on_status(self, status):
        if not hasattr(status, "retweeted_status"):
            if hasattr(status, "extended_tweet"):
                full_status = status.extended_tweet
                hashtags_str = ' '.join([thing['text'] for thing in full_status['entities']["hashtags"]])
                text_no_comma = ''.join((''.join(full_status['full_text'].split("\n"))).split(","))
            else:
                hashtags_str = ' '.join([thing['text'] for thing in status.entities["hashtags"]])
                text_no_comma = ''.join((''.join(status.text.split("\n"))).split(","))
            row = status.user.name + ", " + text_no_comma + ", " + hashtags_str + ", " + str(status.created_at) + "\n"
            outfile_name = os.path.join(self.raw_data_path, "{:%Y-%B-%d}".format(datetime.now()) + ".csv")
            outfile = open(outfile_name, "a+", encoding="utf-8")
            outfile.write(row)
            outfile.close()

    def on_error(self, status_code):
        if status_code == 420:
            time.sleep(60)
            return True
        else:
            return True
