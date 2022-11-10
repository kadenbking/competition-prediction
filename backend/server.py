from flask import Flask
from flask import request
from prediction.nba_predict import *
# from util.leagues import *

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to compeition-prediction!"

# GET TEAMS ROUTE
# @app.route('/get-teams', methods=['GET'])
# def mlb():
#     league = request.args['league']
#     try:
#         teams = getTeams(league)
#         return teams
#     except KeyError:
#         return 'Error! Something is not working...'

# PREDICT ROUTE
@app.route('/predict/<league>/<homeTeam>/<awayTeam>', methods=['GET'])
def mlb(league=None, homeTeam=None, awayTeam=None):
    # home_team = request.args['homeTeam']
    # away_team = request.args['awayTeam']
    try:
        if (league == "nba"):
            outcome = predict_nba_game(homeTeam, awayTeam)
            return outcome
        return "League Not Supported."
    except KeyError:
        return 'Error! Something is not working...'

if __name__ == "__main__":
    app.run()