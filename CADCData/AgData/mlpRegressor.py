import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn.metrics import accuracy_score


data = pd.read_csv("Cleaned Data Set.csv")
train = data[data['Years'] < 2000]
train_x = train.drop(columns=['Yield per harvested acre', 'Years', 'Million Bushels Production'])
train_x = pd.get_dummies(train_x, columns=['Crop'])
train_y = train['Yield per harvested acre']

test = data[data['Years'] >= 2000]
test_x = test.drop(columns=['Yield per harvested acre', 'Years', 'Million Bushels Production'])
test_x = pd.get_dummies(test_x, columns=['Crop'])
test_y = test['Yield per harvested acre']

model = MLPRegressor()
parameter_space = {
    'hidden_layer_sizes': [(50,50,50), (50,100,50)],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
}

clf = GridSearchCV(model, parameter_space, n_jobs=-1, cv=3, verbose=10)
clf.fit(train_x, train_y)

print("score: " + str(clf.score(test_x, test_y)))

predictions = clf.predict(test_x)
pred_df = test
pred_df["Predicted Yield per Acre"] = predictions

pred_df.to_csv("predictedYields.csv")

for param in clf.best_params_:
    print(param)
pickle.dump(clf, open("model.sav", 'wb'))


