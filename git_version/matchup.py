from datetime import datetime

class Matchup():
    #game_time = [month, day, hour, minute]
    def __init__(self, name, home_team, away_team, game_time):
        self.debug = False

        self.name = name
        year = 2018
        datetime_gametime = datetime(year, game_time[0], game_time[1], game_time[2], game_time[3])
        self.game_time = datetime_gametime
        self.home_team = home_team
        self.away_team = away_team

        self.tag_track = home_team.tags + away_team.tags
        self.one_hour_til_gametime = False
        self.analyzed = False

    def time_check(self):
        now = datetime.now()

        if self.debug:
            self.one_hour_til_gametime = True
        else:
            seconds_remaining = int((self.game_time - now).seconds)
            days_remaining = int((self.game_time - now).days)
            if days_remaining == 0 and seconds_remaining <= 3600:
                self.one_hour_til_gametime = True
            if days_remaining < 0:
                self.analyzed = True

    def analyze(self, threshold = 0.5):
        self.home_team.analyze(self.game_time, threshold = threshold)
        self.away_team.analyze(self.game_time, threshold = threshold)
        self.analyzed = True

    def characterize(self, twitter_account, print_result = True, send_tweet = True):
        #Want to add some functionality for reporting stats in the tweet
        home_swing = self.home_team.sentiment_1day - self.home_team.sentiment_4day
        away_swing = self.away_team.sentiment_1day - self.away_team.sentiment_4day

        stats_line = ""

        stats_line += "  " + self.home_team.name + " totals\n"
        stats_line += "    4 day: " +str(len(self.home_team.final_tweets_4day)) + ", " + str(self.home_team.positive_4day) + "+ " + str(self.home_team.negative_4day) + "-\n"
        stats_line += "    1 day: " + str(len(self.home_team.final_tweets_1day)) + ", " + str(self.home_team.positive_1day) + "+ " + str(self.home_team.negative_1day) + "-\n"
        stats_line += "    swing: " + f"{home_swing:.{4}}" + "\n"

        stats_line += "  " + self.away_team.name + " totals\n"
        stats_line += "    4 day: " + str(len(self.away_team.final_tweets_4day)) + ", " + str(self.away_team.positive_4day) + "+ " + str(self.away_team.negative_4day) + "-\n"
        stats_line += "    1 day: " + str(len(self.away_team.final_tweets_1day)) + ", " + str(self.away_team.positive_1day) + "+ " + str(self.away_team.negative_1day) + "-\n"
        stats_line += "    swing: " + f"{away_swing:.{4}}"

        if home_swing >= away_swing:
            if print_result: print(self.home_team.name + " predicted win")
            win_line = self.home_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

            if self.debug:
                win_line = "DEBUG TEST at " + datetime.now().strftime("%H:%M:%S") + ": " + self.home_team.name + " predicted win\n"

        else:
            if print_result: print(self.away_team.name + " predicted win")
            win_line = self.away_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

            if self.debug:
                win_line = "DEBUG TEST at " + datetime.now().strftime("%H:%M:%S") + ": " + self.away_team.name + " predicted win\n"
        if print_result:
            print (win_line + stats_line)
        
        if send_tweet:
            twitter_account.api.update_status(win_line + stats_line)