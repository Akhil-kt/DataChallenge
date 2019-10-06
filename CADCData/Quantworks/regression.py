import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import shutil

data = pd.read_csv("sales_week_anon_201909241613.csv")
units = data['sales_units']
data = data.drop(columns=['sales_units'])

model = SVR()
parameter_space = {
    'kernel' : ['linear', 'rbf', 'sigmoid'],
    'shrinking' : [True, False],
    # 'decision_function_shape' : ['ovo', 'ovr']
}


clf = GridSearchCV(model, parameter_space, n_jobs=-1, cv=5, verbose=10)
clf.fit(pd.get_dummies(data), units)

print(clf.get_params)
