import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

PATH = 'mlb-game-results-2022.csv'
df = pd.read_csv(PATH)

X = df.iloc[:, :-1].values
y = df.iloc[:, 2].values

train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=42, train_size=0.8, test_size=0.2, shuffle=True)

svm = SVC(kernel='rbf', C=4)
svm.fit(train_x, train_y)

pickle.dump(svm, open('mlb-model.pkl','wb'))