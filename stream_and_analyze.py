import sys
import os
import tools
from nfl_twitter_tags import nfl_tags_dict
from team import Team
import custom_twitter

if __name__ == "__main__":
    debug = False
    stream_log_filename = "stream_status.txt"
    analysis_log_filename = "analysis_status.txt"
    schedule_filename = "clean_schedule.csv"
    # The following bit of code is my solution to being able to test this without
    # my twitter account keys showing up in the code or having to remember to
    # delete them all the time.
    token_file = sys.argv[1]
    personal_token_list, bot_token_list = tools.get_tokens(token_file)

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
    next_game_time = tools.get_next_game_time(schedule_file)

    if debug:
        matchup_name_list = tools.get_matchups(schedule_file, next_game_time)
        tools.analyze_matchups(matchup_name_list, next_game_time, debug=debug)
    else:
        while True:
        # while (datetime.now() - next_game_time).total_seconds() < 0:
            next_game_time = tools.get_next_game_time(schedule_file)
            tools.get_to_gametime(next_game_time, analysis_log_file)
            matchup_list = tools.get_matchups(schedule_file, next_game_time)
            # TODO analyze all matchups at the current game time
            next_game_time = tools.get_next_game_time(schedule_file)
            # TODO big error here: games don't always start an hour appart
            # TODO get the full matchup list for that day
            # TODO enter a new loop (in a new function) that loops through
            # TODO all matchups for that day and analyzes them when it is time.
