####################################################
#                                                  #
#                     IMPORTS                      #
#                                                  #
####################################################

from sportsipy.mlb.teams import Teams as MLBTeams
from sportsipy.nba.teams import Teams as NBATeams
from sportsipy.nfl.teams import Teams as NFLTeams
from sportsipy.nhl.teams import Teams as NHLTeams



####################################################
#                                                  #
#                     OBJECTS                      #
#                                                  #
####################################################

class MLB:
    def __init__(self):
        teams = str(MLBTeams()).split("\n")
        clean_teams = [team[1:-1] for team in teams]
        self.teams = clean_teams

class NBA:
    def __init__(self):
        teams = str(MLBTeams()).split("\n")
        clean_teams = [team[1:-1] for team in teams]
        self.teams = clean_teams

class NFL:
    def __init__(self):
        teams = str(MLBTeams()).split("\n")
        clean_teams = [team[1:-1] for team in teams]
        self.teams = clean_teams

class NHL:
    def __init__(self):
        teams = str(MLBTeams()).split("\n")
        clean_teams = [team[1:-1] for team in teams]
        self.teams = clean_teams


####################################################
#                                                  #
#                     TESTING                      #
#                                                  #
####################################################
#mlb = MLB().teams
#print(mlb)


