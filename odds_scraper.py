import requests
import json

source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl-preseason").json()
# source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl").json()

# target_bovada_description_line = "Green Bay Packers" + " @ " + "Chicago Bears"
for event in source[0]['events']:
    # if event['description'] == target_bovada_description_line:
    i = 0
    moneyline = False
    while not moneyline:
        try:
            bet_type = event['displayGroups'][0]["markets"][i]['description']
        except:
            print('failed')
        print(bet_type)
        if bet_type == 'Moneyline':
            print("found moneyline")
            moneyline = True
        else:
            print("not moneyline")
            i += 1
    team_1 = event['displayGroups'][0]["markets"][i]["outcomes"][0]["description"]
    odds_1 = event['displayGroups'][0]["markets"][i]["outcomes"][0]["price"]["american"]
    team_2 = event['displayGroups'][0]["markets"][i]["outcomes"][1]["description"]
    odds_2 = event['displayGroups'][0]["markets"][i]["outcomes"][1]["price"]["american"]
    print(team_1 + ' (' + odds_1 + ") " + team_2 + " (" + odds_2 + ")" )
# odds = {team_1: odds_1, team_2: odds_2}
# # print(source['events'])
# with open("ps_odds_data.txt", "w+", errors='ignore') as odf:
#     odf.write(json.dumps(source, indent=4, sort_keys=True))
    # for thing in source[0]:
    #     print(thing)
    #     print(source[0][thing])
    #     odf.write(str(thing) + "\n")

# print(source)