# LoLImprov (TITLE WIP)

Noah Yoshida


### Dependencies
 - Code is written in python2.7
 - All data is in REQUIREMENTS.txt - 'pip install -r REQUIREMENETS.txt'
 - This uses the RiotGames API - in order to use you will need your own
   development API. Get one here:
   https://developer.riotgames.com/



 Ideas:

---

 - Checks how well you are performing vs your average performance, average
   performance of pro players in same role / champ
 - Determines what metrics you are lacking in, shows difference, suggests ways
   to improve
 - Only will give basic feedback and suggestins for now - if more 'subjective' feedback is desired, it will have to implement some ML 

---

Will need to use SQLite or an equivalent to make databases for all of the
static data from the LeagueOfLegends API, such as item codes, mastery codes,
champion codes, and what not.

---

TODO:
- [ ] Make API wrapper for querying relevant data
- [ ] Make databases, (Learn SQL + how to use in Django)
- [ ] Design front-end UI
- [ ] Determine relevant info to query for users
