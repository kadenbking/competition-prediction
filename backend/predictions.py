import pickle
from models.helpers.teamsLists import *

def mlb_predict(home_team, away_team):
    mlbModel = pickle.load(open('models/mlb-model.pkl','rb'))
    team1 = mlbTeams[home_team]
    team2 = mlbTeams[away_team]
    input = [team1, team2]
    outcome = mlbModel.predict([input])
    return f'{outcome[0]}'

def nba_predict(home_team, away_team):
    nbaModel = pickle.load(open('models/nba-model.pkl','rb'))
    team1 = nbaTeams[home_team]
    team2 = nbaTeams[away_team]
    input = [team1, team2]
    outcome = nbaModel.predict([input])
    return f'{outcome[0]}'

def nfl_predict(home_team, away_team):
    nflModel = pickle.load(open('models/nfl-model.pkl','rb'))
    team1 = nflTeams[home_team]
    team2 = nflTeams[away_team]
    input = [team1, team2]
    outcome = nflModel.predict([input])
    return f'{outcome[0]}'

if __name__ == "__main__":
    print(nfl_predict('KCC', 'LVR'))