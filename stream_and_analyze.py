import sys
import tweepy
import custom_twitter
import os
from nfl_twitter_tags import nfl_tags_dict
from team import Team
from datetime import datetime, timedelta
from time import sleep
from matchup import Matchup


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
    newpid = os.fork()
    if newpid == 0:
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

def get_next_game_time(schedule_file):
    current_time = datetime.now()
    game_time = current_time - timedelta(hours = 1)
    with open(schedule_file, "r", encoding='utf-8') as sf:
        sf.readline() # waste the header
        game_line = sf.readline()
        while (current_time - game_time).total_seconds() > 0 and game_line:
            game_list_line = game_line.strip().split(",")
            game_time_str = "".join(game_list_line[:2])
             # subtract an hour to get to central time
            game_time = datetime.strptime(game_time_str, '%m/%d/%Y %H:%M') - timedelta(hours=1)
            game_line = sf.readline()
    return game_time

def get_to_gametime(next_game_time, log_file):
    extra_delay = 5
    one_hour = 60 * 60
    current_time = datetime.now()
    seconds_until_game = int((next_game_time - current_time).total_seconds())
    while seconds_until_game > one_hour:
        sleep_time = int(min(one_hour, seconds_until_game - one_hour))
        log = "{:%Y-%B-%d %H:%M}".format(current_time) + " Going to sleep for " + str(sleep_time + extra_delay) + " seconds!\n"
        log += "    " + str(seconds_until_game) + " seconds until gametime!\n"
        with open(log_file, "a+", encoding='utf-8') as lf:
            lf.write(log)
        sleep(sleep_time)
        sleep(extra_delay)
        current_time = datetime.now()
        seconds_until_game = int((next_game_time - current_time).total_seconds())

def get_matchups(schedule_file, current_game_time):
    # add an hour to get back to eastern time
    current_game_time = current_game_time + timedelta(hours=1)
    current_date_str = current_game_time.strftime('%m/%d/%Y')
    current_time_str = current_game_time.strftime('%H:%M')
    matchup_list = []
    with open(schedule_file, "r", encoding='utf-8') as sf:
        sf.readline() # waste the header
        game_line = sf.readline()
        while game_line:
            game_line_list = [text.strip() for text in game_line.strip().split(",")]
            correct_day = game_line_list[0] == current_date_str
            correct_time = game_line_list[1] == current_time_str
            if correct_day and correct_time:
                matchup_list.append([game_line_list[2].strip(), game_line_list[3].strip()])
            game_line = sf.readline()
    return matchup_list

def analyze_matchups(matchup_name_list, next_game_time, debug=False):
    for m in matchup_name_list:
        home_team = league[m[0]]
        away_team = league[m[1]]
        matchup = Matchup(home_team, away_team, next_game_time, debug=debug)
        matchup.analyze(bot_account, threshold = 0.0, print_result = True, send_tweet = True)

if __name__ == "__main__":
    debug = False
    stream_log_filename = "stream_status.txt"
    analysis_log_filename = "analysis_status.txt"
    schedule_filename = "clean_schedule.csv"
    # The following bit of code is my solution to being able to test this without
    # my twitter account keys showing up in the code or having to remember to
    # delete them all the time.
    token_file = sys.argv[1]
    personal_token_list, bot_token_list = get_tokens(token_file)

    bot_account = custom_twitter.TwitterAccount(bot_token_list[0], bot_token_list[1], bot_token_list[2], bot_token_list[3])

    schedule_file = os.getcwd() + os.sep + "schedule" + os.sep + schedule_filename
    data_path = os.getcwd() + os.sep + "datafiles"
    nfl_tags = []
    league = {}
    for team_name in nfl_tags_dict:
        nfl_tags += nfl_tags_dict[team_name]
        league[team_name] = Team(team_name, nfl_tags_dict[team_name], data_path)

    stream_log = os.getcwd() + os.sep + "logs" + os.sep + stream_log_filename
    # fork_stream(nfl_tags, bot_account, data_path, stream_log)

    analysis_log_file = os.getcwd() + os.sep + "logs" + os.sep + analysis_log_filename
    next_game_time = get_next_game_time(schedule_file)

    if debug:
        matchup_name_list = get_matchups(schedule_file, next_game_time)
        analyze_matchups(matchup_name_list, next_game_time, debug=debug)
    else:
        while True:
        # while (datetime.now() - next_game_time).total_seconds() < 0:
            next_game_time = get_next_game_time(schedule_file)
            get_to_gametime(next_game_time, analysis_log_file)
            matchup_list = get_matchups(schedule_file, next_game_time)
            # TODO analyze all matchups at the current game time
            next_game_time = get_next_game_time(schedule_file)
            # TODO big error here: games don't always start an hour appart
            # TODO get the full matchup list for that day
            # TODO enter a new loop (in a new function) that loops through
            # TODO all matchups for that day and analyzes them when it is time.
