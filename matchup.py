from datetime import datetime
import time
import os

class Matchup():
    def __init__(self, away_team, home_team, game_time):
        # TODO input checking
        self.name = home_team.name + "_v_" + away_team.name + "_" + game_time.strftime('%m-%d')
        self.home_team = home_team
        self.away_team = away_team
        self.game_time = game_time

    def __characterize(self, home_swing, away_swing, twitter_account, print_result, send_tweet, debug):
        if debug:
            timing_start = time.time()
            print("entered matchup.Matchup.__characterize")
        stats_line = ""
        stats_line += "home swing: " + f"{home_swing:.{4}}" + "\n"
        stats_line += "away swing: " + f"{away_swing:.{4}}"

        if home_swing >= away_swing:
            win_line = self.home_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

        else:
            win_line = self.away_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

        if debug:
            output_line = "DEBUG TESTING, IGNORE\n"
        else:
            output_line = ""
        output_line += win_line + stats_line
        if print_result:
            print (output_line)

        home_team_figure_filename = self.home_team.name + "_" + "{:%Y-%B-%d}".format(self.game_time) + ".png"
        home_team_image_path = os.path.join(self.home_team.team_data_directory, home_team_figure_filename)

        away_team_figure_filename = self.away_team.name + "_" + "{:%Y-%B-%d}".format(self.game_time) + ".png"
        away_team_image_path = os.path.join(self.away_team.team_data_directory, away_team_figure_filename)
        images = [home_team_image_path, away_team_image_path]
        image_ids = []
        for image in images:
            res = twitter_account.api.media_upload(image)
            image_ids.append(res.media_id)

        if send_tweet:
            twitter_account.api.update_status(status=output_line, media_ids=image_ids)
        if debug:
            time_elapsed = time.time() - timing_start
            print("matchup.Matchup.__characterize completed in " + "{0:.4f}".format(time_elapsed))

    def analyze(self, twitter_account, analyzed_data_path, threshold = 0.0, print_result = False, send_tweet = True, debug=False):
        if debug:
            timing_start = time.time()
            print("entered matchup.Matchup.analyze")
        home_sentiment_4day, home_sentiment_1day = self.home_team.analyze(self.game_time, analyzed_data_path, threshold=threshold, debug=debug)
        away_sentiment_4day, away_sentiment_1day = self.away_team.analyze(self.game_time, analyzed_data_path, threshold=threshold, debug=debug)
        home_swing = home_sentiment_1day - home_sentiment_4day
        away_swing = away_sentiment_1day - away_sentiment_4day
        self.__characterize(home_swing, away_swing, twitter_account, print_result, send_tweet, debug)
        if debug:
            time_elapsed = time.time() - timing_start
            print("matchup.Matchup.analyze completed in " + "{0:.4f}".format(time_elapsed))

    def __bool__(self):
        return True
