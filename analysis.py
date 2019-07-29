import schedule
import matchup
import twitter
import time

# import debug

matchups = schedule.week_14_matchups

# debug.set_debug(matchups, ["2018-August-27.csv", "2018-August-28.csv", "2018-August-29.csv", "2018-August-30.csv"], print_debug = False)

sentiment_bot = twitter.TwitterClient()

testing = True
all_playing = len(matchups) * [False]
while not all(all_playing):
    for i in range(len(matchups)):
        matchups[i].time_check()
        if matchups[i].one_hour_til_gametime and not matchups[i].analyzed:
            matchups[i].analyze(threshold = 0.00)
            matchups[i].characterize(sentiment_bot, send_tweet = True)
        all_playing[i] = matchups[i].one_hour_til_gametime
    time.sleep(60)
    if testing:
        print("test")
        testing = False