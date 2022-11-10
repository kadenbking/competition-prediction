import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from leagues import NFL


FIELDS_TO_DROP = ['points_allowed', 'points_scored', 'location', 'overtime', 'time_of_possession',
                  'opponent_abbr', 'opponent_name', 'result', 'type']

dataset = NFL().dataset
dataset = dataset.iloc[: , 5:]
X = dataset.drop(columns=FIELDS_TO_DROP)
y = dataset[['points_scored', 'points_allowed']].values
X_train, X_test, y_train, y_test = train_test_split(X, y)
parameters = {'bootstrap': False,
              'min_samples_leaf': 3,
              'n_estimators': 50,
              'min_samples_split': 10,
              'max_features': 'sqrt',
              'max_depth': 6}
model = RandomForestRegressor(**parameters)
model.fit(X_train, y_train)
print(model.predict(X_test).astype(int), y_test)