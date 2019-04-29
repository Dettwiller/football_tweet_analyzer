import os
import shutil
from datetime import datetime, timedelta

import sentiment
import debug as DEBUG
import codecs

class Team():
    def __init__(self, name, tags):
        self.debug = False
        self.debug_print = False

        cwd = os.getcwd()
        self.raw_data_path = cwd + os.sep + "datafiles" + os.sep + "raw"
        self.team_data_path = cwd + os.sep + "datafiles" + os.sep + "team"

        self.debug_file_list = []
        self.debug_start = None
        self.debug_end = None
        self.debug_elapsed = None

        self.team_tweets_file = None

        self.name = name
        self.tags = tags
        self.lower_tag_list = [tag.lower() for tag in (''.join(self.tags)).split('#')[1:]]

        self.relevant_tweets = []
        self.all_tweets_4day = []
        self.all_tweets_1day = []
        self.accepted_tweets_4day = []
        self.accepted_tweets_1day = []
        self.final_tweets_4day = []
        self.final_tweets_1day = []

        self.average_4day_sentiment = 0.0
        self.average_1day_sentiment = 0.0

        self.positive_4day = 0
        self.negative_4day = 0
        self.positive_1day = 0
        self.negative_1day = 0
        self.sentiment_4day = 0.0
        self.sentiment_1day = 0.0

    def __create_team_tweet_file(self, game_time):
        ttf = codecs.open(self.team_tweets_file, "w+", encoding='utf-8', errors='ignore')

        if self.debug:
            relevant_tweet_files = self.debug_file_list
            for relevant_tweet_file in relevant_tweet_files:
                rtf = open(relevant_tweet_file, "r", encoding = 'utf8', errors='ignore')
                for line in rtf:
                    ttf.write(line)
                rtf.close()
            ttf.close()
            self.debug_start, self.debug_end = DEBUG.get_startend_times(self.team_tweets_file)
            self.debug_elapsed = int((self.debug_end - self.debug_start).seconds)

        else:
            relevant_tweet_files = []
            for i in range(1, 5):
                relevant_day = game_time - timedelta(days=i)
                candidate_filename = "{:%Y-%B-%d}".format(relevant_day) + ".csv"
                if os.path.exists(os.path.join(self.raw_data_path, candidate_filename)):
                    relevant_tweet_files += [candidate_filename]
            for relevant_tweet_file in relevant_tweet_files:
                rtf = open(os.path.join(self.raw_data_path, relevant_tweet_file), "r", encoding = 'utf8', errors='ignore')
                for line in rtf:
                    ttf.write(line)
                rtf.close()

            ttf.close()

    def __tag_filter(self):
        with open(self.team_tweets_file, "r", encoding = 'utf-8', errors='ignore') as tweet_file:
            for line in tweet_file:
                list_line = line.split(",")
                clean_list_line = [list_line_i.rstrip("\n").lstrip(" ") for list_line_i in list_line]
                if len(clean_list_line) == 4:
                    hashtags = clean_list_line[2].split(' ')
                    lower_tweet_list = [test_tag.lower() for test_tag in hashtags]
                    if any([tag in lower_tweet_list for tag in self.lower_tag_list]):
                        self.relevant_tweets += [clean_list_line[:]]

        if self.debug and self.debug_print:
            print("Post-tag filtered: " + str(len(self.relevant_tweets)))

    def __time_filter(self, game_time):
        if self.debug:
            for tweet in self.relevant_tweets:
                greenwich_adjustment = timedelta(hours=5)
                tweet_time = datetime.strptime(tweet[-1], '%Y-%m-%d %H:%M:%S') - greenwich_adjustment
                time_from_start = int((tweet_time - self.debug_start).seconds)

                if time_from_start <= self.debug_elapsed:
                    self.all_tweets_4day += [tweet[:]]
                if time_from_start > int(self.debug_elapsed / 2):
                    self.all_tweets_1day += [tweet[:]]

        else:
            for tweet in self.relevant_tweets:
                greenwich_adjustment = timedelta(hours=5)
                tweet_time = datetime.strptime(tweet[-1], '%Y-%m-%d %H:%M:%S') - greenwich_adjustment
                time_till_game = int((game_time - tweet_time).days)

                if time_till_game < 4:
                    self.all_tweets_4day += [tweet[:]]
                if time_till_game < 1:
                    self.all_tweets_1day += [tweet[:]]

        if self.debug and self.debug_print:
            print("Post-time filtered:")
            print("    4 day: " + str(len(self.all_tweets_4day)))
            print("    1 day: " + str(len(self.all_tweets_1day)))

    def __name_filter(self):
        filtered_names = []
        for tweet in self.all_tweets_4day:
            if tweet[0] not in filtered_names:
                self.accepted_tweets_4day += [tweet[:]]
                filtered_names += [tweet[0]]

        filtered_names = []
        for tweet in self.all_tweets_1day:
            if tweet[0] not in filtered_names:
                self.accepted_tweets_1day += [tweet[:]]
                filtered_names += [tweet[0]]

        if self.debug and self.debug_print:
            print("Post-name filtered:")
            print("    4 day: " + str(len(self.accepted_tweets_4day)))
            print("    1 day: " + str(len(self.accepted_tweets_1day)))

    def __add_sentiment(self):
        for tweet_data in self.accepted_tweets_4day:
            tweet_sentiment = sentiment.get_tweet_sentiment(tweet_data[1])
            self.final_tweets_4day += [[tweet_data[0], str(tweet_sentiment), tweet_data[1], tweet_data[2], tweet_data[3]]]

        for tweet_data in self.accepted_tweets_1day:
            tweet_sentiment = sentiment.get_tweet_sentiment(tweet_data[1])
            self.final_tweets_1day += [[tweet_data[0], str(tweet_sentiment), tweet_data[1], tweet_data[2], tweet_data[3]]]

    def __write_final_tweets(self):
        with open(self.team_tweets_file, "w", encoding='utf-8', errors='ignore') as team_file:
            for tweet in self.final_tweets_4day:
                line = ",".join(tweet) + "\n"
                team_file.write(line)

    def __sort_and_count(self, threshold):
        for tweet in self.final_tweets_4day:
            self.average_4day_sentiment += float(tweet[1])
            if float(tweet[1]) > threshold:
                self.positive_4day += 1
            elif float(tweet[1]) < -threshold:
                self.negative_4day += 1

        if len(self.final_tweets_4day) == 0:
            self.average_4day_sentiment = self.average_4day_sentiment / 1.0
        else:
            self.average_4day_sentiment = self.average_4day_sentiment / len(self.final_tweets_4day)

        for tweet in self.final_tweets_1day:
            self.average_1day_sentiment += float(tweet[1])
            if float(tweet[1]) > threshold:
                self.positive_1day += 1
            elif float(tweet[1]) < -threshold:
                self.negative_1day += 1

        if len(self.final_tweets_1day) == 0:
            self.average_1day_sentiment = self.average_1day_sentiment / 1.0
        else:
            self.average_1day_sentiment = self.average_1day_sentiment / len(self.final_tweets_1day)

    def __team_sentiment(self):
        total_4day_tweets = len(self.final_tweets_4day)
        if total_4day_tweets == 0: total_4day_tweets = 1

        total_1day_tweets = len(self.final_tweets_1day)
        if total_1day_tweets == 0: total_1day_tweets = 1

        self.sentiment_4day = float(self.positive_4day / total_4day_tweets) - float(self.negative_4day / total_4day_tweets)
        self.sentiment_1day = float(self.positive_1day / total_1day_tweets) - float(self.negative_1day / total_1day_tweets)

    def analyze(self, game_time, threshold = 0.5):
        str_date = "{:%Y-%B-%d}".format(datetime.now())
        self.team_tweets_file = self.team_data_path + os.sep + self.name + "_" + str_date + ".csv"

        self.__create_team_tweet_file(game_time)
        self.__tag_filter()
        self.__time_filter(game_time)
        self.__name_filter()
        self.__add_sentiment()
        self.__write_final_tweets()
        self.__sort_and_count(threshold)
        self.__team_sentiment()