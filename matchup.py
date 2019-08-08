from datetime import datetime

class Matchup():
    def __init__(self, away_team, home_team, game_time, debug = False):
        # TODO input checking
        self.debug = debug
        self.name = home_team.name + "_v_" + away_team.name + "_" + game_time.strftime('%m-%d')
        self.home_team = home_team
        self.away_team = away_team
        self.game_time = game_time

    def __characterize(self, home_swing, away_swing, twitter_account, print_result, send_tweet):
        stats_line = ""
        if self.debug:
            stats_line += "DEBUG TESTING, IGNORE\n"
        stats_line += "swing: " + f"{home_swing:.{4}}" + "\n"
        stats_line += "swing: " + f"{away_swing:.{4}}"

        if home_swing >= away_swing:
            if print_result: print(self.home_team.name + " predicted win")
            win_line = self.home_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

        else:
            if print_result: print(self.away_team.name + " predicted win")
            win_line = self.away_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"
        if print_result:
            print (win_line + stats_line)

        if send_tweet:
            twitter_account.api.update_status(win_line + stats_line)

    def update_teams(self, league):
        self.home_team = league[self.home_team.name]
        self.away_team = league[self.away_team.name]

    def analyze(self, twitter_account, threshold = 0.0, print_result = False, send_tweet = True):


        home_sentiment_4day, home_sentiment_1day = self.home_team.analyze(self.game_time, threshold = threshold)
        away_sentiment_4day, away_sentiment_1day = self.away_team.analyze(self.game_time, threshold = threshold)

        home_swing = home_sentiment_1day - home_sentiment_4day
        away_swing = away_sentiment_4day - away_sentiment_1day
        self.__characterize(home_swing, away_swing, twitter_account, print_result, send_tweet)

    def __bool__(self):
        return True
