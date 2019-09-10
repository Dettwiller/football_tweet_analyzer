import sentiment
import os

data_path = "C:" + os.sep + "Users" + os.sep + "User" + os.sep + "Documents" + os.sep + "NFL_twitter_analysis" + os.sep + "datafiles_2019"
raw_data_path = data_path + os.sep + "raw"
analyzed_data_path = data_path + os.sep + "bert_analyzed"
bert_data_path = "C:" + os.sep  + "Users" + os.sep  + "User" + os.sep  + "Documents" + os.sep  + "NFL_twitter_analysis" + os.sep  + "bert_data"

sentiment.bert_analyze_raw_files(raw_data_path, analyzed_data_path, bert_data_path)
