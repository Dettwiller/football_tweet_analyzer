import re
import os
from datetime import datetime, timedelta
import subprocess

import tools
from textblob import TextBlob
from textblob import Blobber

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    # create TextBlob object of passed tweet text
    cleaned_tweet = clean_tweet(tweet)
    analysis = TextBlob(cleaned_tweet)
    return analysis.sentiment.polarity

def get_last_analyzed_file(analyzed_data_path):
    start_date = datetime(2019, 8, 2)
    today = datetime.now()
    while today >= start_date:
        candidate_filename = "{:%Y-%B-%d}".format(today) + ".csv"
        if os.path.exists(os.path.join(analyzed_data_path, candidate_filename)):
            return today
        else:
            today -= timedelta(days=1)
    return start_date

def analyze_raw_files(raw_data_path, analyzed_data_path):
    start_date = get_last_analyzed_file(analyzed_data_path)
    today = datetime.now()
    tweet_files = tools.get_dated_files(raw_data_path, today, start_date)
    for tweet_file in tweet_files:
        with open(os.path.join(raw_data_path, tweet_file), "r", encoding="utf-8", errors='ignore') as rtf:
            with open(os.path.join(analyzed_data_path, tweet_file), "w+", encoding='utf-8', errors='ignore') as atf:
                line = rtf.readline() # user, content, hashtags, date
                while line:
                    list_line = line.strip().split(",")
                    if len(list_line) == 4:
                        tweet_sentiment = get_tweet_sentiment(list_line[1])
                        output_list_line = [list_line[1], list_line[2], str(tweet_sentiment), list_line[3]]
                        # content, hashtags, sentiment, date
                        atf.write(",".join(output_list_line) + "\n")
                    line = rtf.readline()

def write_bert_input_files(raw_data_path, relevant_raw_tweet_files, bert_input_data_path):
    atf = open(os.path.join(bert_input_data_path, "get_test.csv"), "w+", encoding='utf-8', errors='ignore')
    for tweet_file in relevant_raw_tweet_files:
        with open(os.path.join(raw_data_path, tweet_file), "r", encoding="utf-8", errors='ignore') as rtf:
            line = rtf.readline() # user, content, hashtags, date
            while line:
                list_line = line.strip().split(",")
                if len(list_line) == 4:
                    tweet_content = clean_tweet(list_line[1])
                    atf.write(tweet_content + "\n")
                line = rtf.readline()
    atf.close()

def execute_bert(bert_input_data_path, bert_output_data_path):
    base_bert_dir  = "C:" + os.sep  + "Users" + os.sep  + "User" + os.sep  + "Documents" + os.sep
    base_bert_dir += "Python Programs" + os.sep  + "bert_sentiment" + os.sep + "original"

    bert_test_dir = base_bert_dir + os.sep + "BERT-fine-tuning-for-twitter-sentiment-analysis" + os.sep + "test_bert"
    init_checkpoint = base_bert_dir + os.sep  + "BERT-fine-tuning-for-twitter-sentiment-analysis" + os.sep  + "model"

    bert_config_file = base_bert_dir + os.sep + "cased_L-12_H-768_A-12" + os.sep  + "bert_config.json"
    vocab_file = base_bert_dir + os.sep + "cased_L-12_H-768_A-12" + os.sep  + "vocab.txt"

    original_dir = os.getcwd()
    os.chdir(bert_test_dir)
    argument_list = [
        "python",
        "run_classifier.py",
        "--task_name=twitter",
        "--do_predict=true",
        "--do_lower_case=false",
        "--data_dir=" + bert_input_data_path,
        "--vocab_file=" + vocab_file,
        "--bert_config_file=" + bert_config_file,
        "--init_checkpoint=" + init_checkpoint,
        "--max_seq_length=64",
        "--output_dir=" + bert_output_data_path
    ]
    subprocess.run(argument_list)
    os.chdir(original_dir)

def write_bert_analyzed_output(raw_data_path, analyzed_data_path, relevant_raw_tweet_files, bert_output_data_path):
    bof = open(os.path.join(bert_output_data_path, "test_results.tsv"), "r", encoding='utf-8', errors='ignore')
    for tweet_file in relevant_raw_tweet_files:
        with open(os.path.join(raw_data_path, tweet_file), "r", encoding="utf-8", errors='ignore') as rtf:
            with open(os.path.join(analyzed_data_path, tweet_file), "w+", encoding='utf-8', errors='ignore') as atf:
                rtf_line = rtf.readline() # user, content, hashtags, date
                while rtf_line:
                    rtf_list_line = rtf_line.strip().split(",")
                    if len(rtf_list_line) == 4:
                        bert_result = bof.readline() # negative, positive
                        bert_result_list = bert_result.strip().split()
                        try:
                            bert_sentiment = float(bert_result_list[1]) - float(bert_result_list[0])
                        except:
                            print(bert_result)
                        output_list_line = [rtf_list_line[1], rtf_list_line[2], str(bert_sentiment), rtf_list_line[3]]
                        # content, hashtags, sentiment, date
                        atf.write(",".join(output_list_line) + "\n")
                    rtf_line = rtf.readline()
    bof.close()

def bert_analyze_raw_files(raw_data_path, analyzed_data_path, bert_data_path):
    bert_input_data_path = bert_data_path + os.sep + "input"
    bert_output_data_path = bert_data_path + os.sep + "output"
    start_date = get_last_analyzed_file(analyzed_data_path)
    today = datetime.now()
    tweet_files = tools.get_dated_files(raw_data_path, today, start_date)
    write_bert_input_files(raw_data_path, tweet_files, bert_input_data_path)
    execute_bert(bert_input_data_path, bert_output_data_path)
    write_bert_analyzed_output(raw_data_path, analyzed_data_path, tweet_files, bert_output_data_path)