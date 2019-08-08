from unicodedata import normalize
from datetime import datetime

'''
    This script cleans the dirty schedule in 'nfl_schedule.csv'
    to provide a date and time for each game in 'clean_schedule.csv'.
    The dirty file was created by copying and pasting each week's
    schedule into a spreadsheet and then keeping just the text.
'''

input_file = "nfl_schedule.csv"
output_file = "clean_schedule.csv"
with open(input_file, "rt", encoding='utf-8') as inf:
    with open(output_file, "w+", encoding='utf-8') as ouf:
        output_line = "date, time (ET), away, home, analyzed\n"
        ouf.write(output_line)
        line = normalize('NFKD', inf.readline().strip())
        while line:
            output_line = ""
            list_line = line.split(",") # [day, time, home team, away team]

            # handle the date
            if list_line[0]:
                curr_date = datetime.strptime(list_line[0], '%a %b %d') # Thu Sep 5
                curr_str_date = curr_date.strftime('%m/%d/2019')
            output_line += curr_str_date + ", "

            # handle the time
            game_time = datetime.strptime(list_line[1], '%I:%M %p') # 8:20 pm
            str_game_time = game_time.strftime('%H:%M')
            output_line += str_game_time + ","

            # copy the teams
            output_line += ",".join(list_line[2:]) + "\n"
            ouf.write(output_line)

            line = normalize('NFKD', inf.readline().strip())