import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from leagues import NFL


# FIELDS_TO_DROP = ['away_runs', 'home_runs', 'date', 'location',
#                   'losing_abbr', 'losing_name', 'winner', 'winning_abbr',
#                   'winning_name']

# X = dataset.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()

print(NFL().dataset)