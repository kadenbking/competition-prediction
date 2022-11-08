from flask import Flask
from flask import request
from leagues.mlb import *

app = Flask(__name__)

# Home API Route
@app.route('/')
def home():
    return "Welcome to compeition-prediction!"

# MLB API Route
@app.route('/mlb', methods=['GET'])
def mlb():
    # home_team = request.args['homeTeam']
    # away_team = request.args['awayTeam']
    try:
        teams = getTeams()
        return teams
    except KeyError:
        return 'Major League Baseball'

# NBA API Route

# NFL API Route

# NHL API Route

# NCAAF API Route

# NCAAB API Route

if __name__ == "__main__":
    app.run()