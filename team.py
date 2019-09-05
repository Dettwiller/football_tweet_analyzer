import os
from datetime import datetime, timedelta
import tools
import sentiment
import pandas as pd
import time
import matplotlib.pyplot as plt

class Team():
    def __init__(self, team_name, twitter_tags, team_data_directory):
        # TODO any input checking necessary
        self.team_data_directory = team_data_directory
        self.name = "_".join(team_name.split())
        self.tags = twitter_tags
        self.lower_tag_list = [tag.lower() for tag in (''.join(twitter_tags)).split('#')[1:]]
    
    def __tag_filter(self, analyzed_tweets_file, debug=False):
        if debug:
            timing_start = time.time()
            print("entered team.Team.__tag_filter")
        sentiments = []
        times = []
        with open(analyzed_tweets_file, "r", encoding = 'utf-8', errors='ignore') as tweet_file:
            for line in tweet_file:
                list_line = line.split(",")
                clean_list_line = [list_line_i.rstrip("\n").lstrip(" ") for list_line_i in list_line]
                if len(clean_list_line) == 4:
                    # content, hashtags, sentiment, date
                    hashtags = clean_list_line[1].split(' ')
                    lower_tweet_list = [test_tag.lower() for test_tag in hashtags]
                    if any([tag in lower_tweet_list for tag in self.lower_tag_list]):
                        sentiments += [float(clean_list_line[2])]
                        times += [datetime.strptime(clean_list_line[3], '%Y-%m-%d %H:%M:%S')] # 2019-08-02 14:12:28
        
        if debug:
            time_elapsed = time.time() - timing_start
            print("team.Team.__tag_filter completed in " + "{0:.4f}".format(time_elapsed))
        return sentiments, times

    def __plot_sentiment(self, rolling_4day, rolling_1day, game_time):
        plotted_days = 1
        start_plot = datetime.now() - timedelta(days=plotted_days)
        relevant_rolling_4day = rolling_4day.loc[start_plot : datetime.now()]
        relevant_rolling_1day = rolling_1day.loc[start_plot : datetime.now()]
        title_font_size = 14
        label_font_size = 10
        fig_size = (6.4, 4.8)
        figure_filename = self.name + "_" + "{:%Y-%B-%d}".format(game_time)
        figure_file = os.path.join(self.team_data_directory, figure_filename)
        # max_length = max(len(rolling_1day), len(rolling_4day))
        # x = range(max_length)
        title = self.name + " Sentiment " + "{:%Y-%B-%d}".format(game_time)
        plt.figure(figsize=fig_size)
        plt.plot(relevant_rolling_4day, linewidth=1.0, color='b', label='4 day rolling average')
        plt.plot(relevant_rolling_1day, linewidth=1.0, color='r', label='1 day rolling average')
        plt.ylabel('Sentiment', fontsize=label_font_size)
        plt.xlabel('Previous ' + str(plotted_days) + ' day(s)', fontsize=label_font_size)
        plt.xticks([], [])
        plt.title(title, fontsize=title_font_size)
        plt.legend(loc='best', fancybox=True)
        plt.tight_layout()
        plt.savefig(figure_file)
        plt.close()

    def analyze(self, game_time, analyzed_data_path, start_date = datetime(2019, 8, 2), debug=False):
        if debug:
            timing_start = time.time()
            print("entered team.Team.analyze")
        analyzed_files = tools.get_dated_files(analyzed_data_path, game_time, start_time=start_date)
        sentiments = []
        times = []
        for tweet_file in analyzed_files:
            new_sentiments, new_times = self.__tag_filter(os.path.join(analyzed_data_path, tweet_file), debug=debug)
            sentiments += new_sentiments
            times += new_times
        sentiment_dataframe = pd.DataFrame(sentiments, index=times, columns=['Sentiment'])
        sentiment_dataframe = sentiment_dataframe.sort_index()
        rolling_4day = sentiment_dataframe['Sentiment'].rolling('4d').mean()
        rolling_1day = sentiment_dataframe['Sentiment'].rolling('1d').mean()
        self.__plot_sentiment(rolling_4day, rolling_1day, game_time)
        if debug:
            time_elapsed = time.time() - timing_start
            print("team.Team.analyze completed in " + "{0:.4f}".format(time_elapsed))
        return rolling_4day[-1], rolling_1day[-1]