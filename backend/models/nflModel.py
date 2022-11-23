import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from helpers.plot_helpers import plot_learning_curve
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

PATH = '/Users/kadenking/School/Fall2022/competition-prediction/backend/models/datasets/nfl-game-results-2018-2021.csv'

#SVC Model
df = pd.read_csv(PATH)

X = df.iloc[:, :-1].values
y = df.iloc[:, 2].values

train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=42, train_size=0.8, test_size=0.2, shuffle=True)

svm = SVC(kernel='rbf', C=4)
svm.fit(train_x, train_y)

accuracy = accuracy_score(test_y, svm.predict(test_x))
precision = precision_score(test_y, svm.predict(test_x))
recall = recall_score(test_y, svm.predict(test_x))

print('Accuracy: ', accuracy)
print('Precision: ', precision)
print('Recall: ', recall)

plot_learning_curve(
    svm,
    "SVM",
    train_x,
    train_y,
    scoring="accuracy",
    ylim=(0.3, 1.01),
    cv=5,
    n_jobs=4
)

plt.savefig('nflModel-svm.png')


#Decision Tree
df = pd.read_csv(PATH)

X = df.iloc[:, :-1].values
y = df.iloc[:, 2].values

train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=42, train_size=0.8, test_size=0.2, shuffle=True)

tree = DecisionTreeClassifier()
tree.fit(train_x, train_y)

accuracy = accuracy_score(test_y, tree.predict(test_x))
precision = precision_score(test_y, tree.predict(test_x))
recall = recall_score(test_y, tree.predict(test_x))

print('Accuracy: ', accuracy)
print('Precision: ', precision)
print('Recall: ', recall)

plot_learning_curve(
    tree,
    "Decision Tree",
    train_x,
    train_y,
    scoring="accuracy",
    ylim=(0.3, 1.01),
    cv=5,
    n_jobs=4
)

plt.savefig('nflModel-tree.png')


#Neural Network
df = pd.read_csv(PATH)

X = df.iloc[:, :-1].values
y = df.iloc[:, 2].values

train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=42, train_size=0.8, test_size=0.2, shuffle=True)

mlp = MLPClassifier(hidden_layer_sizes=(100, 70, 120), max_iter=300000)
mlp.fit(train_x, train_y)

accuracy = accuracy_score(test_y, mlp.predict(test_x))
precision = precision_score(test_y, mlp.predict(test_x))
recall = recall_score(test_y, mlp.predict(test_x))

print('Accuracy: ', accuracy)
print('Precision: ', precision)
print('Recall: ', recall)

plot_learning_curve(
    mlp,
    "Neural Network",
    train_x,
    train_y,
    scoring="accuracy",
    ylim=(0.3, 1.01),
    cv=5,
    n_jobs=4
)

plot = plt.plot([accuracy, precision, recall])
plt.savefig('nflModel-neuralnet.png')



pickle.dump(svm, open('nfl-model.pkl','wb'))