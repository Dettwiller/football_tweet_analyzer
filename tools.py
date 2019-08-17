import sys
import tweepy
import custom_twitter
import os
from datetime import datetime, timedelta
from time import sleep
from matchup import Matchup
import sentiment
import time

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

def create_matchup_from_schedule_line(schedule_line, league):
    game_list_line = schedule_line.strip().split(",")
    game_time_str = "".join(game_list_line[:2])
    # subtract an hour to get to central time
    game_time = datetime.strptime(game_time_str, '%m/%d/%Y %H:%M') - timedelta(hours=1)
    matchup = Matchup(league[game_list_line[2].strip()], league[game_list_line[3].strip()], game_time)
    return matchup

def get_next_matchup(schedule_file, league, previous_matchup=False, debug=False):
    if debug:
        timing_start = time.time()
        print("entered tools.get_next_matchup")
    current_time = datetime.now()
    with open(schedule_file, "r", encoding='utf-8') as sf:
        sf.readline() # waste the header
        game_line = sf.readline()
        matchup = create_matchup_from_schedule_line(game_line, league)
        if previous_matchup:
            while matchup.name != previous_matchup.name:
                game_line = sf.readline()
                matchup = create_matchup_from_schedule_line(game_line, league)
            game_line = sf.readline()
            matchup = create_matchup_from_schedule_line(game_line, league)
        else:
            while (current_time - matchup.game_time).total_seconds() > 0 and game_line:
                game_line = sf.readline()
                matchup = create_matchup_from_schedule_line(game_line, league)
    if debug:
        time_elapsed = time.time() - timing_start
        print("tools.get_next_matchup completed in " + "{0:.4f}".format(time_elapsed))
    return matchup

def get_to_analysis(next_matchup, log_file, raw_data_path, analyzed_data_path, bert_data_path = "", debug=False):
    if debug:
        timing_start = time.time()
        print("entered tools.get_to_analysis")
    extra_delay = 5 # seconds
    one_hour = 60 * 60 # 60 seconds / minute * 60 minutes / hour
    current_time = datetime.now()
    if debug:
        seconds_until_analysis = 1
    else:
        seconds_until_analysis = int((next_matchup.game_time- current_time).total_seconds()) - one_hour # analyze an hour before kickoff
    while seconds_until_analysis > 0:
        sleep_time = int(min(6 * one_hour, seconds_until_analysis))
        if debug:
            log = "DEBUG: " + "{:%Y-%B-%d %H:%M}".format(current_time) + " Going to sleep for " + str(sleep_time + extra_delay) + " seconds!\n"
            log += "    DEBUG: " + str(seconds_until_analysis) + " seconds until " + next_matchup.name + " analysis time!\n"
        else:
            log = "{:%Y-%B-%d %H:%M}".format(current_time) + " Going to sleep for " + str(sleep_time + extra_delay) + " seconds!\n"
            log += "    " + str(seconds_until_analysis) + " seconds until " + next_matchup.name + " analysis time!\n"
        with open(log_file, "a+", encoding='utf-8') as lf:
            lf.write(log)
        print(log)
        sleep(sleep_time)
        sleep(extra_delay)
        current_time = datetime.now()
        # permanent code (uncomment please)
        if bert_data_path:
            # pass
            sentiment.bert_analyze_raw_files(raw_data_path, analyzed_data_path, bert_data_path)
        else:
            sentiment.analyze_raw_files(raw_data_path, analyzed_data_path)

        # temporary code
        # if debug:
        #     temp_data_path = "C:" + os.sep + "Users" + os.sep + "User" + os.sep + "Documents" + os.sep + "NFL_twitter_analysis" + os.sep + "datafiles_2019"
        #     bert_analyzed_data_path = temp_data_path + os.sep + "bert_analyzed"
        #     sentiment.bert_analyze_raw_files(raw_data_path, bert_analyzed_data_path, bert_data_path)
        #     sentiment.analyze_raw_files(raw_data_path, analyzed_data_path)

        if debug:
            seconds_until_analysis = -1
        else:
            seconds_until_analysis = int((next_matchup.game_time - current_time).total_seconds()) - one_hour # analyze an hour before kickoff
    if debug:
        time_elapsed = time.time() - timing_start
        print("tools.get_to_analysis completed in " + "{0:.4f}".format(time_elapsed))

def get_dated_files(file_directory, terminating_time, start_time = datetime(2019, 8, 2)):
    files = []
    while (terminating_time - start_time).days >= 0:
        candidate_filename = "{:%Y-%B-%d}".format(start_time) + ".csv"
        if os.path.exists(os.path.join(file_directory, candidate_filename)):
            files += [candidate_filename]
        start_time += timedelta(days=1)
    return files