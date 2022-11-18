from prediction.sims.mlb_sim import simulate_game
import sys

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

def predict_mlb_game(home_team, away_team):
    win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id = \
        simulate_game('2022', '2022', home_team, away_team, display_info=True)
    return "{} {} has a {}% chance of beating {} {}.".format(win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id)

if __name__ == "__main__":
    win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id = \
        simulate_game(sys.argv[1], sys.argv[3], sys.argv[2], sys.argv[4], display_info=True)
    print("{} {} has a {}% chance of beating {} {}.".format(win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id))