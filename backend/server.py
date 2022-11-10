from flask import Flask
from flask import request
from util.leagues import *

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to compeition-prediction!"

# GET TEAMS ROUTE
@app.route('/get-teams', methods=['GET'])
def mlb():
    league = request.args['league']
    try:
        teams = getTeams(league)
        return teams
    except KeyError:
        return 'Error! Something is not working...'

# PREDICT ROUTE
# @app.route('/predict', methods=['GET'])
# def mlb():
#     league = request.args['league']
#     home_team = request.args['homeTeam']
#     away_team = request.args['awayTeam']
#     try:
#         outcome = predictResult(league, home_team, away_team)
#         return outcome
#     except KeyError:
#         return 'Error! Something is not working...'

if __name__ == "__main__":
    app.run()