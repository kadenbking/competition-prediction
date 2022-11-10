# All commented code is broken due to bad support from sportsipy API
import pandas as pd
from sportsipy.mlb.teams import Teams as MLBTeams
# from sportsipy.nba.teams import Teams as NBATeams
from sportsipy.nfl.teams import Teams as NFLTeams
from sportsipy.nhl.teams import Teams as NHLTeams
from sportsipy.ncaaf.teams import Teams as NCAAFTeams
# from sportsipy.ncaab.teams import Teams as NCAABTeams

class MLB:
    def __init__(self):
        teams = MLBTeams()
        dataset = pd.DataFrame()
        for team in teams:
            dataset = pd.concat([dataset, team.schedule.dataframe])
        teams_array = str(MLBTeams()).split("\n")
        cleaned_teams_array = [team[1:-1] for team in teams_array]
        self.teams = cleaned_teams_array
        self.dataset = dataset

# class NBA:
#     def __init__(self):
#         teams = str(NBATeams()).split("\n")
#         clean_teams = [team[1:-1] for team in teams]
#         self.teams = clean_teams

class NFL:
    def __init__(self):
        teams = NFLTeams(2021)
        dataset = pd.DataFrame()
        for team in teams:
            dataset = pd.concat([dataset, team.schedule.dataframe])
        teams_array = str(NFLTeams()).split("\n")
        self.teams = teams_array
        self.dataset = dataset

class NHL:
    def __init__(self):
        teams = NHLTeams()
        dataset = pd.DataFrame()
        for team in teams:
            dataset = pd.concat([dataset, team.schedule.dataframe])
        teams_array = str(NHLTeams()).split("\n")
        self.teams = teams_array
        self.dataset = dataset

class NCAAF:
    def __init__(self):
        teams = NCAAFTeams(2021)
        dataset = pd.DataFrame()
        for team in teams:
            dataset = pd.concat([dataset, team.schedule.dataframe])
        teams_array = str(NCAAFTeams()).split("\n")
        self.teams = teams_array
        self.dataset = dataset

# class NCAAB:
#     def __init__(self):
#         teams = str(NCAABTeams()).split("\n")
#         self.teams = teams

def getTeams(league):
    if (league == "mlb"):
        return MLB().teams
    if (league == "nfl"):
        return NFL().teams
    if (league == "nhl"):
        return NHL().teams
    if (league == "ncaaf"):
        return NCAAF().teams
    return []
