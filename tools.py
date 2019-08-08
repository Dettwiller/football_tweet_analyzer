import sys
import tweepy
import custom_twitter
import os
from datetime import datetime, timedelta
from time import sleep
from matchup import Matchup

from nfl_twitter_tags import nfl_tags_dict


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

def fork_stream(tags, twitter_account, data_path, stream_log):
    newpid = os.fork() # TODO this does not work on windows
    if newpid == 0:
        failures = 0
        while True:
            try:
                log = "{:%Y-%B-%d %H:%M}".format(datetime.now()) + " streaming...\n"
                with open(stream_log, "a+", encoding='utf-8') as sl:
                    sl.write(log)
                print(log)
                stream(tags, twitter_account, data_path)
            except:
                failures += 1
                log = "{:%Y-%B-%d %H:%M}".format(datetime.now()) + " stream failure " + str(failures) + "\n\n"
                with open(stream_log, "a+", encoding='utf-8') as sl:
                    sl.write(log)
                print(log)

def create_matchup_from_schedule_line(schedule_line):
    game_list_line = schedule_line.strip().split(",")
    game_time_str = "".join(game_list_line[:2])
    # subtract an hour to get to central time
    game_time = datetime.strptime(game_time_str, '%m/%d/%Y %H:%M') - timedelta(hours=1)
    matchup = Matchup(game_list_line[2].strip(), game_list_line[3].strip(), game_time)
    return matchup

def get_next_matchup(schedule_file, previous_matchup=False):
    current_time = datetime.now()
    with open(schedule_file, "r", encoding='utf-8') as sf:
        sf.readline() # waste the header
        game_line = sf.readline()
        matchup = create_matchup_from_schedule_line(game_line)
        if previous_matchup:
            while matchup.name != previous_matchup.name:
                game_line = sf.readline()
                matchup = create_matchup_from_schedule_line(game_line)
            game_line = sf.readline()
            matchup = create_matchup_from_schedule_line(game_line)
        else:
            while (current_time - matchup.game_time).total_seconds() > 0 and game_line:
                game_line = sf.readline()
                matchup = create_matchup_from_schedule_line(game_line)
    return matchup

def get_to_analysis(next_matchup, log_file, league):
    extra_delay = 5 # seconds
    one_hour = 60 * 60 # 60 seconds / minute * 60 minutes / hour
    current_time = datetime.now()
    seconds_until_gametime = int((next_matchup.game_time- current_time).total_seconds())
    while seconds_until_gametime > one_hour:
        sleep_time = int(min(one_hour, seconds_until_gametime))
        log = "{:%Y-%B-%d %H:%M}".format(current_time) + " Going to sleep for " + str(sleep_time + extra_delay) + " seconds!\n"
        log += "    " + str(seconds_until_gametime) + " seconds until gametime!\n"
        with open(log_file, "a+", encoding='utf-8') as lf:
            lf.write(log)
        sleep(sleep_time)
        sleep(extra_delay)
        current_time = datetime.now()
        for team_name in league:
            league[team_name].update_team_tweet_files()
        seconds_until_gametime = int((next_matchup.game_time - current_time).total_seconds())
    return league

# def get_matchups(schedule_file, current_game_time):
#     # add an hour to get back to eastern time
#     current_game_time = current_game_time + timedelta(hours=1)
#     current_date_str = current_game_time.strftime('%m/%d/%Y')
#     current_time_str = current_game_time.strftime('%H:%M')
#     matchup_list = []
#     with open(schedule_file, "r", encoding='utf-8') as sf:
#         sf.readline() # waste the header
#         game_line = sf.readline()
#         while game_line:
#             game_line_list = [text.strip() for text in game_line.strip().split(",")]
#             correct_day = game_line_list[0] == current_date_str
#             correct_time = game_line_list[1] == current_time_str
#             if correct_day and correct_time:
#                 matchup_list.append([game_line_list[2].strip(), game_line_list[3].strip()])
#             game_line = sf.readline()
#     return matchup_list
