import pickle
from models.mlbTeams import mlbTeams

def mlb_predict(home_team, away_team):
    mlbModel = pickle.load(open('models/mlb-model.pkl','rb'))
    team1 = mlbTeams[home_team]
    team2 = mlbTeams[away_team]
    input = [team1, team2]
    pred = mlbModel.predict([input])
    winning_team = home_team if pred[0] == 1 else away_team
    losing_team = home_team if pred[0] == 0 else away_team
    outcome = {
        'winningTeam': winning_team,
        'losingTeam': losing_team
    }
    return outcome


if __name__ == "__main__":
    print(mlb_predict('KCR', 'ATL'))