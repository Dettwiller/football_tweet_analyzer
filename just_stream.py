import sys
import tweepy
import custom_twitter
import os
from nfl_twitter_tags import nfl_tags_dict
from datetime import datetime

def get_tokens(token_file):
    with open(token_file, "r", encoding='utf-8') as tf:
        file_lines = tf.readlines()
    personal_keys = ["", "", "", ""] # consumer, consumer secret, access, access secret
    bot_keys = ["", "", "", ""]
    for i in range(4):
        personal_keys[i] = file_lines[i + 1].split()[-1].strip()
        bot_keys[i] = file_lines[i + 7].split()[-1].strip()
    return personal_keys, bot_keys


def stream(tags, twitter_account, data_path):
    stream_listener = custom_twitter.MyStreamListener(twitter_account, data_path)
    stream = tweepy.Stream(auth = twitter_account.auth, listener = stream_listener)
    stream.filter(track=tags)

def launch_stream(tags, twitter_account, data_path, stream_log):
    failures = 0
    while True:
        try:
            log = "{:%Y-%B-%d}".format(datetime.now()) + " streaming...\n"
            with open(stream_log, "a+", encoding='utf-8') as sl:
                sl.write(log)
            stream(tags, twitter_account, data_path)
        except:
            failures += 1
            log = "{:%Y-%B-%d}".format(datetime.now()) + " stream failure " + str(failures) + "\n\n"
            with open(stream_log, "a+", encoding='utf-8') as sl:
                sl.write(log)

if __name__ == "__main__":
    stream_log_filename = "stream_status.txt"
    # The following bit of code is my solution to being able to test this without
    # my twitter account keys showing up in the code or having to remember to
    # delete them all the time.
    token_file = sys.argv[1]
    personal_token_list, bot_token_list = get_tokens(token_file)

    bot_account = custom_twitter.TwitterAccount(bot_token_list[0], bot_token_list[1], bot_token_list[2], bot_token_list[3])
    data_path = os.getcwd() + os.sep + "datafiles"
    nfl_tags = []
    league = {}
    for team_name in nfl_tags_dict:
        nfl_tags += nfl_tags_dict[team_name]

    stream_log = os.getcwd() + os.sep + "logs" + os.sep + stream_log_filename
    launch_stream(nfl_tags, bot_account, data_path, stream_log)
