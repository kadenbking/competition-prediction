from prediction.sims.mlb_sim import *
import sys

def predict_mlb_game_stats(home_team, away_team):
    win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id = \
        simulate_game('2021', '2021', home_team, away_team, display_info=True)
    return "{} {} has a {}% chance of beating {} {}.".format(win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id)

if __name__ == "__main__":
    win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id = \
        simulate_game(sys.argv[1], sys.argv[3], sys.argv[2], sys.argv[4], display_info=True)
    print("{} {} has a {}% chance of beating {} {}.".format(win_team_year, win_team_id, win_team_percent, lose_team_year, lose_team_id))