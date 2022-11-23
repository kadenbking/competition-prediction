import pandas as pd
import numpy as np
from prediction.sims.utils.data_scrapers.nba_scraper import getTeamStats
# from data_scrapers.nba_scraper import getTeamStats UNCOMMENT THIS LINE TO RUN THIS FILE

def get_team_data(team_id, year, header=False):
    team_stats_tuple = getTeamStats(team_id, year)

    regular_stats_raw = np.array(team_stats_tuple[0].iloc[1,2:])
    regular_stats = list(map(lambda value: float(value), regular_stats_raw))
    regular_stats_header = team_stats_tuple[1][2:]

    advanced_stats = np.array(team_stats_tuple[2].iloc[0, 1:-2])
    advanced_stats_header_raw = team_stats_tuple[3][1:-2]
    advanced_stats_header = list(map(lambda tuple: tuple[1], advanced_stats_header_raw))

    stats_full = np.concatenate((regular_stats, advanced_stats), axis=None)
    header_full = np.concatenate((regular_stats_header, advanced_stats_header), axis=None)

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
