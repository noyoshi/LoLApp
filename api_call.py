# -*- coding: utf-8 -*-

# Generic API query to get relevant data

import GET_TOKEN as _token
import requests

def query(region, ext):
    
    url = "https://{region}.api.riotgames.com/{ext}".format(region=region, ext=ext)
    data = requests.get(url)
