import pandas as pd
import numpy as np
from prediction.sims.utils.data_scrapers.mlb_scraper import getTeamStats

def get_team_data(team_id, year, header=False):
    team_stats_tuple = getTeamStats(team_id, year)

    batting_stats_raw = np.array(team_stats_tuple[0].iloc[1,5:])
    batting_stats = list(map(lambda value: float(value), batting_stats_raw))
    batting_stats_header = team_stats_tuple[1][5:]

    pitching_stats = np.array(team_stats_tuple[2].iloc[1,4:])
    pitching_stats_header = team_stats_tuple[3][4:]

    stats_full = np.concatenate((batting_stats, pitching_stats), axis=None)
    header_full = np.concatenate((batting_stats_header, pitching_stats_header), axis=None)

    if header == True:
        return header_full
    else:
        return stats_full


def get_all_teams_data(teams, year):
    team_stats_array = []
    for team in teams:
        team_stats = get_team_data(team, year)
        team_stats_array.append(team_stats)
    return team_stats_array


def generate_dataframe(rows, header):
    df = pd.DataFrame(rows, columns=header)
    return df
