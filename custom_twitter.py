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

    def __init__(self, twitter_account_object):
        tweepy.StreamListener.__init__(self)
        self.twitter_object = twitter_account_object
        self.raw_data_path = os.getcwd() + os.sep + "datafiles" + os.sep + "raw"

    def on_status(self, status):
        if not hasattr(status, "retweeted_status"):
            try:
                full_status = self.tweet_object.api.get_status(status.id_str, tweet_mode='extended')
            except:
                full_status = None

            if hasattr(full_status, "full_text"):
                hashtags_str = ' '.join([thing['text'] for thing in full_status.entities["hashtags"]])
                text_no_comma = ''.join((''.join(full_status.full_text.split("\n"))).split(","))
                row = full_status.user.name + ", " + text_no_comma + ", " + hashtags_str + ", " + str(status.created_at) + "\n"
                outfile = open(os.path.join(self.raw_data_path, "{:%Y-%B-%d}".format(datetime.now()) + ".csv"), "a+", encoding="utf8")
                outfile.write(row)
                outfile.close()

    def on_error(self, status_code):
        if status_code == 420:
            time.sleep(60)
            return True
        else:
            return True
