

import urllib 

class player(object):
    
    def __init__(self, acct_id, summoner_name, rank):
        self.acct_id = acct_id
        self.summoner_name = summoner_name
        self.rank = rank
    

    def get_id(self):
        return self.acct_id

    def get_name(self):
        return self.name 

    def get_rank(self):
        return self.rank
