from datetime import datetime
import time
import os
import requests

class Matchup():
    def __init__(self, away_team, home_team, game_time):
        # TODO input checking
        self.name = home_team.name + "_v_" + away_team.name + "_" + game_time.strftime('%m-%d')
        self.home_team = home_team
        self.away_team = away_team
        self.game_time = game_time
        self.regular_season_start = datetime(2019, 8, 31)

    def __get_moneyline_index(self, event):
        i = 0
        moneyline = False
        while not moneyline:
            try:
                bet_type = event['displayGroups'][0]["markets"][i]['description']
            except:
                return None
            if bet_type == 'Moneyline':
                moneyline = True
            else:
                i += 1
        return i

    def __get_odds(self):
        try:
            if self.game_time < datetime(2019, 8, 31):
                source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl-preseason").json()
            else:
                source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl").json()
            plain_away_name = " ".join(self.away_team.name.split("_"))
            plain_home_name = " ".join(self.home_team.name.split("_"))
            target_bovada_description_line = plain_away_name + " @ " + plain_home_name
            for event in source[0]['events']:
                if event['description'] == target_bovada_description_line:
                    moneyline_index = self.__get_moneyline_index(event)
                    if moneyline_index is not None:
                        team_1 = event['displayGroups'][0]["markets"][moneyline_index]["outcomes"][0]["description"]
                        odds_1 = event['displayGroups'][0]["markets"][moneyline_index]["outcomes"][0]["price"]["american"]
                        team_2 = event['displayGroups'][0]["markets"][moneyline_index]["outcomes"][1]["description"]
                        odds_2 = event['displayGroups'][0]["markets"][moneyline_index]["outcomes"][1]["price"]["american"]
                    else:
                        raise ValueError("No Moneyline")
            if self.away_team.name != "_".join(team_1.split()):
                print("expected away team name: " + self.away_team.name)
                print("got: " + "_".join(team_1.split()))
            if self.home_team.name != "_".join(team_2.split()):
                print("expected away team name: " + self.home_team.name)
                print("got: " + "_".join(team_2.split()))
            odds = {self.away_team.name: odds_1, self.home_team.name: odds_2}
        except:
            odds = {self.away_team.name: "NA", self.home_team.name: "NA"}
        return odds

    def __get_tweet_content(self, away_swing, home_swing, odds, debug):
        if debug:
            output_line = "DEBUG TESTING, IGNORE\n"
        else:
            output_line = ""
        stats_line = ""
        stats_line += self.home_team.name + " (" + odds[self.home_team.name] + ") swing: " + f"{home_swing:.{4}}" + "\n"
        stats_line += self.away_team.name + " (" + odds[self.away_team.name] + ") swing: " + f"{away_swing:.{4}}"

        if home_swing >= away_swing:
            win_line = self.home_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

        else:
            win_line = self.away_team.name + " predicted win at " + datetime.now().strftime("%H:%M:%S") + "\n"

        output_line += win_line + stats_line
        return output_line

    def __create_plots(self):
        home_team_figure_filename = self.home_team.name + "_" + "{:%Y-%B-%d}".format(self.game_time) + ".png"
        home_team_image_path = os.path.join(self.home_team.team_data_directory, home_team_figure_filename)

        away_team_figure_filename = self.away_team.name + "_" + "{:%Y-%B-%d}".format(self.game_time) + ".png"
        away_team_image_path = os.path.join(self.away_team.team_data_directory, away_team_figure_filename)
        images = [home_team_image_path, away_team_image_path]
        return images
    
    def __send_tweet(self, twitter_account, tweet_text, tweet_images):
        image_ids = []
        for image in tweet_images:
            res = twitter_account.api.media_upload(image)
            image_ids.append(res.media_id)

        twitter_account.api.update_status(status=tweet_text, media_ids=image_ids)

    def __log_odds(self, odds, odds_file, away_swing, home_swing):
        output_string = "{:%Y-%B-%d %H:%M}".format(self.game_time) + ","
        output_string += self.away_team.name + "," + odds[self.away_team.name] + "," + f"{away_swing:.{4}}" + ","
        output_string += self.home_team.name + "," + odds[self.home_team.name] + "," + f"{home_swing:.{4}}" + "\n"
        with open(odds_file, "a+", encoding='utf-8', errors='ignore') as of:
            of.write(output_string)

    def __characterize(self, home_swing, away_swing, twitter_account, odds_file, print_result, send_tweet, debug):
        if debug:
            timing_start = time.time()
            print("entered matchup.Matchup.__characterize")

        odds = self.__get_odds()
        tweet_text = self.__get_tweet_content(away_swing, home_swing, odds, debug)
        tweet_images = self.__create_plots()
        
        if send_tweet:
            self.__send_tweet(twitter_account, tweet_text, tweet_images)

        self.__log_odds(odds, odds_file, away_swing, home_swing)

        if debug:
            time_elapsed = time.time() - timing_start
            print("matchup.Matchup.__characterize completed in " + "{0:.4f}".format(time_elapsed))

    def analyze(self, twitter_account, analyzed_data_path, odds_file, print_result = False, send_tweet = True, debug=False):
        if debug:
            timing_start = time.time()
            print("entered matchup.Matchup.analyze")
        home_sentiment_4day, home_sentiment_1day = self.home_team.analyze(self.game_time, analyzed_data_path, debug=debug)
        away_sentiment_4day, away_sentiment_1day = self.away_team.analyze(self.game_time, analyzed_data_path, debug=debug)
        home_swing = home_sentiment_1day - home_sentiment_4day
        away_swing = away_sentiment_1day - away_sentiment_4day
        self.__characterize(home_swing, away_swing, twitter_account, odds_file, print_result, send_tweet, debug)
        if debug:
            time_elapsed = time.time() - timing_start
            print("matchup.Matchup.analyze completed in " + "{0:.4f}".format(time_elapsed))

    def __bool__(self):
        return True
