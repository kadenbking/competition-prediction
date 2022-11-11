from flask import Flask
from flask import request
# from prediction.mlb_predict import *
from prediction.nba_predict import *

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to compeition-prediction!"

# PREDICT ROUTE
@app.route('/predict/<league>/<homeTeam>/<awayTeam>', methods=['GET'])
def mlb(league=None, homeTeam=None, awayTeam=None):
    try:
        # if (league == "mlb"):
        #     outcome = predict_mlb_game(homeTeam, awayTeam)
        #     return outcome
        if (league == "nba"):
            outcome = predict_nba_game(homeTeam, awayTeam)
            return outcome
        return "League Not Supported."
    except KeyError:
        return 'Error! Something is not working...'

if __name__ == "__main__":
    app.run()