import pickle
from models.teamsLists import *

def mlb_predict(home_team, away_team):
    mlbModel = pickle.load(open('models/mlb-model.pkl','rb'))
    team1 = mlbTeams[home_team]
    team2 = mlbTeams[away_team]
    input = [team1, team2]
    outcome = mlbModel.predict([input])
    return f'{outcome[0]}'


if __name__ == "__main__":
    print(mlb_predict('KCR', 'ATL'))