import tweepy
import custom_twitter

def forever_stream(tags, auth_tokens):
    # TODO test the damn thing
    while True:
        try:
            twitter_account = custom_twitter.TwitterAccount(auth_tokens[0], auth_tokens[1], auth_tokens[2], auth_tokens[3])
            stream_listener = custom_twitter.MyStreamListener(twitter_account)
            stream = tweepy.Stream(auth = twitter_account.auth, listener = stream_listener)
            stream.filter(track=tags)
        except:
            # TODO track failure information (log file?)
            pass



if __name__ == "__main__":
    # TODO: fork a stream to gather data
    # TODO: loop through games and perform analysis if time_until_game < 1 hour
    # NOTE: Games in clean_schedule.csv are in chronological order
    pass