# -*- coding: utf-8 -*-

# This will update the static database, with the most recent codes for
# champions, items, masteries, runes, etc

import GET_TOKEN as _token
import requests

API_KEY = _token.GET_KEY()

headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": API_KEY,
    "Accept-Language": "en-US,en;q=0.8",
    "tags": "all"
}

region = "na1"
ext = "lol/static-data/v3/champions"
url = "https://{region}.api.riotgames.com/{ext}".format(region=region, ext=ext)
data = requests.get(url, headers=headers)
print data.json()
