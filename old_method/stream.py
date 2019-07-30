import tweepy

import twitter
from cfb_data import SEC
# from cfb_data import week_13_opponents

tags = []
for team in SEC:
    tags += SEC[team].tags

# for team in week_2_opponents:
    # tags += week_2_opponents[team].tags

# for team in week_13_opponents:
#     tags += week_13_opponents[team].tags

api = twitter.BotAccount()

myStreamListener = twitter.MyStreamListener(api)
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=tags)
