import requests as rq
import json

# Declaring variables
headers = {
    'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
}

# You can get list of match IDs from schedule.py
gameIDs = ['107417059263300159', '107417059263300165', '107417059263300141', '107417059263300119', '107417059263300171',
           '107417059263365741', '107417059263365715', '107417059263300145', '107417059263300123', '107417059263365733',
           '107417059263300155', '107417059263300175', '107417059263300131', '107417059263300139', '107417059263365739',
           '107417059263300157', '107417059263300167', '107417059263365737', '107417059263300117', '107417059263365713',
           '107417059263365735', '107417059263300151', '107417059263300129', '107417059263300143', '107417059263365729',
           '107417059263300173', '107417059263300153', '107417059263365725', '107417059263365719', '107417059263300133',
           '107417059263300135', '107417059263300169', '107417059263431353', '107417059263365753', '107417059263365775',
           '107417059263365785', '107417059263365791', '107417059263365773', '107417059263431343', '107417059263431349',
           '107417059263365747', '107417059263365789', '107417059263365745', '107417059263365767', '107417059263431367',
           '107417059263365797', '107417059263431341', '107417059263365743', '107417059263431363', '107417059263431339',
           '107417059263431361', '107417059263365777', '107417059263365765', '107417059263365757', '107417059263431365',
           '107417059263365783', '107417059263365793', '107417059263431355', '107417059263365755', '107417059263365769',
           '107417059263365799', '107417059263365779', '107417059263431357', '107417059263365751', '107417059263431347',
           '107417059263365763', '107417059263365787', '107417059263365771', '107417059263365749', '107417059263431359',
           '107417059263365781', '107417059263365801', '107417059263431351', '107417059263365759', '107417059263431345',
           '107417059263365761', '107417059263365795', '107417293272826572', '107417293272826578', '107417293272826584']

parameters = {
    'hl': 'en-US',
    'gameId': ''
}

print(len(gameIDs))