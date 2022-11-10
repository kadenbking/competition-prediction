import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import urllib.request

def getTeamStats(team_id, year):
    team = team_id.upper()
    url = "https://www.baseball-reference.com/teams/" + team + "/" + year + ".shtml"

    with urllib.request.urlopen(url) as response:
        r = response.read().decode('latin-1')

    content = re.sub(r'(?m)^\<!--.*\n?', '', r)
    content = re.sub(r'(?m)^\-->.*\n?', '', content)

    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.findAll('table')
    
    batting_index = 0
    pitching_index = 1
    
    batting_table = tables[batting_index]
    pitching_table = tables[pitching_index]

    batting_df = pd.read_html(str(batting_table))[0]
    pitching_df = pd.read_html(str(pitching_table))[0]

    batting_totals_df = batting_df.iloc[-5:].apply(np.roll, shift=1)
    pitching_totals_df = pitching_df.iloc[-3:].apply(np.roll, shift=1)

    batting_header = batting_totals_df.columns.values.tolist()
    pitching_header = pitching_totals_df.columns.values.tolist()

    return batting_totals_df, batting_header, pitching_totals_df, pitching_header

if __name__ == "__main__":
    stuff = getTeamStats('BAL', '2021')
    print(stuff)

    # stuff[0].to_csv('mlb.csv')
    # stuff[2].to_csv('mlb1.csv')

