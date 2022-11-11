import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from data_scrapers.mlb_scraper import getTeamStats

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

# TODO: Create model to output team score
def generate_team_score(df):
    return 1

# def generate_teams_training_data(teams, header, year):
#     all_teams_data = get_all_teams_data(teams, year)
#     training_df = generate_dataframe(all_teams_data, header)
#     return training_df


# def clean_up_df(df):
#     cols = []
#     efg_count = 0
#     tov_count = 0
#     ftfga_count = 0
#     for column in df.columns:
#         if column == 'eFG%':
#             cols.append('eFG%_' + str(efg_count))
#             efg_count += 1
#             continue
#         if column == 'TOV%':
#             cols.append('TOV%_' + str(tov_count))
#             tov_count += 1
#             continue
#         if column == 'FT/FGA':
#             cols.append('FT/FGA_' + str(ftfga_count))
#             ftfga_count += 1
#             continue
#         cols.append(column)
#     df.columns = cols
#     return df


# def feature_scaled_df(df):
#     for column in df:
#         df[column] = df[column].apply(lambda x: x/df[column].max())
#     return df


# def predict(X, W):
#     return np.dot(X, W.T)


# def train(X, Y, epochs, l_rate):
#     W = np.zeros(X.shape[1])
#     m = X.shape[0]
#     for epoch in range(epochs):
#         h = predict(X, W)
#         loss = h - Y
#         error = np.sum(loss ** 2) / (2*m)
#         if epoch%1000 == 0 or epoch+1 == epochs:
#             print("Epoch {}, Error: {}".format(epoch, error))
#         gradient = np.dot(X.T, loss) / m
#         W_delta = l_rate * gradient
#         W -= W_delta
#     return W


# def predictWins(weights, X):
#     predictions = predict(X, weights)
#     # print(predictions)
#     return predictions


if __name__ == '__main__':

    # CODE TO GENERATE DF
    # df_header = get_team_data('KCR', '2021', header=True)
    # teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SFG', 'SEA', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
    # all_teams_stats = get_all_teams_data(teams, '2021')
    # df = generate_dataframe(all_teams_stats, df_header)
    # df.to_csv("all_2021_teams.csv")

    # USE THIS AS DF FOR TESTING AND TRAINING
    df = pd.read_csv('all_2021_teams.csv')
    # print(df)

    df_header = get_team_data('KCR', '2021', header=True)
    df_row = [get_team_data('KCR', '2021')]
    team_df = generate_dataframe(df_row, df_header)


    X = df.drop(['W'], axis=1)
    Y = df['W']
    train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state=42, train_size=0.96, test_size=0.03, shuffle=True)

    scaler = MinMaxScaler()
    train_data = scaler.fit_transform(train_x)
    test_data = scaler.fit_transform(test_x)

    svc = SVC(kernel='rbf')
    svc.fit(train_data, train_y)

    pred = svc.predict(team_df)

    accuracy = accuracy_score(test_y, pred)

    print(accuracy)
