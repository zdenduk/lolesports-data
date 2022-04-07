import requests as rq
import json

# Declaring variables
headers = {
    'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
}
parameters = {
    'hl': 'en-US'
}

# API endpoint
getLeagues = 'https://esports-api.lolesports.com/persisted/gw/getLeagues'

# Storing the request into 'data' variable
data = rq.get(getLeagues, params=parameters, headers=headers)
data = data.json()['data']['leagues']

lecID = 0
for i in data:
    for key, value in i.items():
        if value == 'LEC':
            lecID = i['id']

print(lecID)
