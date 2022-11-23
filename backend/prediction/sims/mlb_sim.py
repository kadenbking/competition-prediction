import random
import pickle
from prediction.sims.utils.mlb_utils import get_team_data, generate_dataframe

def getTeamDf(team_id, year):
    df_header = get_team_data(team_id, year, header=True)
    df_row = [get_team_data(team_id, year)]
    return generate_dataframe(df_row, df_header)

def team_score(team_id, year):
    df = getTeamDf(team_id, year)
    score = float(df['W'])
    return score

def simulate_game(t1_year, t2_year, t1_id, t2_id, epochs=100000, home_variation_max=100, away_variation_max=100, display_info=False):
    
    if display_info:
        print("Simulation Presets:")
        print("Epochs: {}".format(epochs))
        print("Home Team Variation Range Max: {}".format(home_variation_max))
        print("Away Team Variation Range Max: {}".format(away_variation_max))
        print()

    t1_metric = team_score(t1_id, t1_year)
    t2_metric = team_score(t2_id, t2_year)

    if display_info:
        print('{} has a CORWIN score of {}'.format(t1_id, t1_metric))
        print('{} has a CORWIN score of {}'.format(t2_id, t2_metric))
        print()
    t1_wins = 0
    t2_wins = 0

    for i in range(epochs):
        t1_random_variation = random.randint(0, home_variation_max) / 10
        t2_random_variation = random.randint(0, away_variation_max) / 10
        t1_final_metric = t1_metric + t1_random_variation
        t2_final_metric = t2_metric + t2_random_variation

        if t1_final_metric > t2_final_metric:
            t1_wins +=1
        else:
            t2_wins +=1

    if display_info:
        print('In {} simulated games, {}: {} wins, {}: {} wins'.format(epochs, t1_id, t1_wins, t2_id, t2_wins))
    if t1_wins > t2_wins:
        return t1_year, t1_id, float(t1_wins)/float(epochs/100), t2_year, t2_id
    else:
        return t2_year, t2_id, float(t2_wins)/float(epochs/100), t1_year, t1_id

def predict_game(home_team, away_team):
    mlbModel = pickle.load(open('/Users/kadenking/School/Fall2022/competition-prediction/models/mlb-model.pkl','rb'))

    mlbTeams = {
        'ARI': 1,
        'ATL': 2,
        'BAL': 3,
        'BOS': 4,
        'CHC': 5,
        'CHW': 6,
        'CIN': 7,
        'CLE': 8,
        'COL': 9,
        'DET': 10,
        'HOU': 11,
        'KCR': 12,
        'LAA': 13,
        'LAD': 14,
        'MIA': 15,
        'MIL': 16,
        'MIN': 17,
        'NYM': 18,
        'NYY': 19,
        'OAK': 20,
        'PHI': 21,
        'PIT': 22,
        'SDP': 23,
        'SFG': 24,
        'SEA': 25,
        'STL': 26,
        'TBR': 27,
        'TEX': 28,
        'TOR': 29,
        'WSN': 30,
    }

    team1 = mlbTeams[home_team]
    team2 = mlbTeams[away_team]

    input = [team1, team2]

    outcome = mlbModel.predict([input])
    return f'Result - {outcome}'

if __name__ == "__main__":
    predict_game('KCR', 'LAA')