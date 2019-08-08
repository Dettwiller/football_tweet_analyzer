import os
from datetime import datetime, timedelta

import sentiment

class Team():
    def __init__(self, team_name, twitter_tags, data_path):
        # TODO any input checking necessary

        self.raw_data_path = data_path + os.sep + "raw"
        self.team_data_path = data_path + os.sep + "team"

        self.name = "_".join(team_name.split())
        self.tags = twitter_tags
        self.lower_tag_list = [tag.lower() for tag in (''.join(twitter_tags)).split('#')[1:]]

    def update_team_tweet_files(self):
        today = datetime.now()
        str_date = "{:%Y-%B-%d}".format(today)
        team_tweets_file = self.team_data_path + os.sep + self.name + "_" + str_date + ".csv"
        relevant_raw_tweet_files = []
        if today.hour < 2:
            yesterday = today - timedelta(days=1)
            candidate_filename = "{:%Y-%B-%d}".format(yesterday) + ".csv"
            if os.path.exists(os.path.join(self.raw_data_path, candidate_filename)):
                relevant_raw_tweet_files += [candidate_filename]
        candidate_filename = "{:%Y-%B-%d}".format(today) + ".csv"
        if os.path.exists(os.path.join(self.raw_data_path, candidate_filename)):
            relevant_raw_tweet_files += [candidate_filename]

        ttf = open(team_tweets_file, "a+", encoding='utf-8', errors='ignore')
        all_lines = ttf.readlines()
        last_tweet_content = all_lines[-1].split(",")[1] # date and time, content, sentiment score
        for relevant_tweet_file in relevant_raw_tweet_files:
            with open(os.path.join(self.raw_data_path, relevant_tweet_file), "r", encoding = 'utf8', errors='ignore') as rtf:
                line = rtf.readline() # user, content, hashtags, date
                while line.split(",")[1] != last_tweet_content and line: # get to new tweets
                    line = rtf.readline()
                while line: # read until end of file
                    line = rtf.readline()
                    list_line = line.split(",")
                    relevant_to_team = self.__determine_relevance_of_tweet(list_line)
                    if relevant_to_team:
                        tweet_sentiment = sentiment.get_tweet_sentiment(list_line[1])
                        output_line = list_line[-1] + "," + list_line[1] + "," + str(tweet_sentiment) + "\n"
                        ttf.write(output_line)
        ttf.close()

    def __determine_relevance_of_tweet(self, tweet_line_list):
        relevant_to_team = False
        clean_list_line = [list_line_i.rstrip("\n").lstrip(" ") for list_line_i in tweet_line_list]
        if len(clean_list_line) == 4:
            hashtags = clean_list_line[2].split(' ')
            lower_tweet_list = [test_tag.lower() for test_tag in hashtags]
            if any([tag in lower_tweet_list for tag in self.lower_tag_list]):
                relevant_to_team = True
        return relevant_to_team


    def __create_team_tweet_file(self, game_time, team_tweets_file):
        ttf = open(team_tweets_file, "w+", encoding='utf-8', errors='ignore')
        # get the raw tweets from the last 4 days
        relevant_raw_tweet_files = []
        for i in range(1, 5):
            relevant_day = game_time - timedelta(days=i)
            candidate_filename = "{:%Y-%B-%d}".format(relevant_day) + ".csv"
            if os.path.exists(os.path.join(self.raw_data_path, candidate_filename)):
                    relevant_raw_tweet_files += [candidate_filename]
            for relevant_tweet_file in relevant_raw_tweet_files:
                rtf = open(os.path.join(self.raw_data_path, relevant_tweet_file), "r", encoding = 'utf8', errors='ignore')
                for line in rtf:
                    ttf.write(line)
                rtf.close()
        ttf.close()

    def __tag_filter(self, team_tweets_file):
        with open(team_tweets_file, "r", encoding = 'utf-8', errors='ignore') as tweet_file:
            for line in tweet_file:
                list_line = line.split(",")
                clean_list_line = [list_line_i.rstrip("\n").lstrip(" ") for list_line_i in list_line]
                if len(clean_list_line) == 4:
                    hashtags = clean_list_line[2].split(' ')
                    lower_tweet_list = [test_tag.lower() for test_tag in hashtags]
                    if any([tag in lower_tweet_list for tag in self.lower_tag_list]):
                        relevant_tweets += [clean_list_line[:]]
        return relevant_tweets

    def __time_filter(self, game_time, relevant_tweets):
        all_tweets_4day = []
        all_tweets_1day = []
        for tweet in relevant_tweets:
            greenwich_adjustment = timedelta(hours=5)
            tweet_time = datetime.strptime(tweet[-1], '%Y-%m-%d %H:%M:%S') - greenwich_adjustment
            time_till_game = int((game_time - tweet_time).days)

            if time_till_game < 4:
                all_tweets_4day += [tweet[:]]
            if time_till_game < 1:
                all_tweets_1day += [tweet[:]]
        return all_tweets_4day, all_tweets_1day

    def __name_filter(self, all_tweets_4day, all_tweets_1day):
        accepted_tweets_4day = []
        accepted_tweets_1day = []
        filtered_names = []
        for tweet in all_tweets_4day:
            if tweet[0] not in filtered_names:
                accepted_tweets_4day += [tweet[:]]
                filtered_names += [tweet[0]]

        filtered_names = []
        for tweet in all_tweets_1day:
            if tweet[0] not in filtered_names:
                accepted_tweets_1day += [tweet[:]]
                filtered_names += [tweet[0]]
        return accepted_tweets_4day, accepted_tweets_1day

    def __add_sentiment(self, accepted_tweets_4day, accepted_tweets_1day):
        final_tweets_4day = []
        final_tweets_1day = []
        for tweet_data in accepted_tweets_4day:
            tweet_sentiment = sentiment.get_tweet_sentiment(tweet_data[1])
            final_tweets_4day += [[tweet_data[0], str(tweet_sentiment), tweet_data[1], tweet_data[2], tweet_data[3]]]

        for tweet_data in accepted_tweets_1day:
            tweet_sentiment = sentiment.get_tweet_sentiment(tweet_data[1])
            final_tweets_1day += [[tweet_data[0], str(tweet_sentiment), tweet_data[1], tweet_data[2], tweet_data[3]]]

        return final_tweets_4day, final_tweets_1day

    def __write_final_tweets(self, team_tweets_file, tweets_4day):
        with open(team_tweets_file, "w", encoding='utf-8', errors='ignore') as team_file:
            for tweet in tweets_4day:
                line = ",".join(tweet) + "\n"
                team_file.write(line)

    def __sort_and_count(self, tweets_4day, tweets_1day, threshold):
        average_4day_sentiment = 0.0
        average_1day_sentiment = 0.0
        positive_4day = 0
        negative_4day = 0
        positive_1day = 0
        negative_1day = 0
        for tweet in tweets_4day:
            average_4day_sentiment += float(tweet[1])
            if float(tweet[1]) > threshold:
                positive_4day += 1
            elif float(tweet[1]) < -threshold:
                negative_4day += 1

        if len(tweets_4day) == 0:
            average_4day_sentiment = average_4day_sentiment / 1.0
        else:
            average_4day_sentiment = average_4day_sentiment / len(tweets_4day)

        for tweet in tweets_1day:
            average_1day_sentiment += float(tweet[1])
            if float(tweet[1]) > threshold:
                positive_1day += 1
            elif float(tweet[1]) < -threshold:
                negative_1day += 1

        if len(tweets_1day) == 0:
            average_1day_sentiment = average_1day_sentiment / 1.0
        else:
            average_1day_sentiment = average_1day_sentiment / len(tweets_1day)
        return [positive_4day, negative_4day, average_4day_sentiment], [positive_1day, negative_1day, average_1day_sentiment]

    def __team_sentiment(self, tweets_4day, tweets_1day, results_4day, results_1day):
        positive_4day = results_4day[0]
        negative_4day = results_4day[1]
        # average_4day_sentiment = results_4day[2]

        positive_1day = results_1day[0]
        negative_1day = results_1day[1]
        # average_1day_sentiment = results_1day[2]

        total_4day_tweets = len(tweets_4day)
        if total_4day_tweets == 0: total_4day_tweets = 1

        total_1day_tweets = len(tweets_1day)
        if total_1day_tweets == 0: total_1day_tweets = 1

        sentiment_4day = float(positive_4day / total_4day_tweets) - float(negative_4day / total_4day_tweets)
        sentiment_1day = float(positive_1day / total_1day_tweets) - float(negative_1day / total_1day_tweets)
        return sentiment_4day, sentiment_1day

    def analyze(self, game_time, threshold = 0.0):
        str_date = "{:%Y-%B-%d}".format(datetime.now())
        team_tweets_file = self.team_data_path + os.sep + self.name + "_" + str_date + ".csv"

        self.__create_team_tweet_file(game_time, team_tweets_file)
        relevant_tweets = self.__tag_filter(team_tweets_file)
        tweets_4day, tweets_1day = self.__time_filter(game_time, relevant_tweets)
        tweets_4day, tweets_1day = self.__name_filter(tweets_4day, tweets_1day)
        tweets_4day, tweets_1day = self.__add_sentiment(tweets_4day, tweets_1day)
        self.__write_final_tweets(team_tweets_file, tweets_4day)
        results_4day, results_1day = self.__sort_and_count(tweets_4day, tweets_1day, threshold)
        sentiment_4day, sentiment_1day = self.__team_sentiment(tweets_4day, tweets_1day, results_4day, results_1day)
        return sentiment_4day, sentiment_1day

    def new_analyze(self, game_time, threshold = 0.0):
        relevant_team_tweet_files = []
        for i in range(1, 5):
            relevant_day = game_time - timedelta(days=i)
            candidate_filename = self.team_data_path + os.sep + self.name + "_" + "{:%Y-%B-%d}".format(relevant_day) + ".csv"
            if os.path.exists(os.path.join(self.raw_data_path, candidate_filename)):
                relevant_team_tweet_files += [candidate_filename]
        average_4day_sentiment = 0.0
        average_1day_sentiment = 0.0
        positive_4day = 0
        negative_4day = 0
        positive_1day = 0
        negative_1day = 0
        greenwich_adjustment = timedelta(hours=5)
        for team_tweet_file in relevant_team_tweet_files:
            rtf = open(os.path.join(self.raw_data_path, relevant_tweet_file), "r", encoding = 'utf8', errors='ignore')
            for line in rtf:
                analyzed_tweet = line.split(",")
                tweet_time = datetime.strptime(analyzed_tweet[0], '%Y-%m-%d %H:%M:%S') - greenwich_adjustment
                time_till_game = int((game_time - tweet_time).days)
                # TODO determine whether it is a 1day, 4day, or not considered
                if time_till_game <
            rtf.close()