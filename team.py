import os

class Team():
    def __init__(self, team_name, twitter_tags, data_path):
        # TODO any input checking necessary

        self.raw_data_path = data_path + os.sep + "raw"
        self.team_data_path = data_path + os.sep + "team"

        self.name = team_name
        self.tags = twitter_tags
