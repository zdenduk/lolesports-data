import requests as rq
import json

# Declaring variables
headers = {
    'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
}

# You can get leagueId from leagues.py
parameters = {
    'hl': 'en-US',
    'leagueId': '98767991302996019'
}

# API endpoint
getSchedule = 'https://esports-api.lolesports.com/persisted/gw/getSchedule'

# Storing the request into 'data' variable
data = rq.get(getSchedule, params=parameters, headers=headers)
data = data.json()['data']['schedule']['events']

ids = []
for event in data:
    ids.append(event['match']['id'])

print(ids)
