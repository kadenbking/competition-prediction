import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import urllib.request

def getTeamStats(team_id, year):
    team = team_id.upper()
    url = "https://www.basketball-reference.com/teams/" + team + "/" + year + ".html"

    with urllib.request.urlopen(url) as response:
        r = response.read().decode('latin-1')

    content = re.sub(r'(?m)^\<!--.*\n?', '', r)
    content = re.sub(r'(?m)^\-->.*\n?', '', content)

    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.findAll('table')
    
    stats_index = 2
    misc_index = 3
    
    stats_table = tables[stats_index]
    misc_table = tables[misc_index]

    stats_df = pd.read_html(str(stats_table))[0]
    misc_df = pd.read_html(str(misc_table))[0]

    stats_header = stats_df.columns.values.tolist()
    misc_header = misc_df.columns.values.tolist()

    return stats_df, stats_header, misc_df, misc_header

if __name__ == "__main__":
    stuff = getTeamStats('GSW', '2020')
    # print(stuff)
