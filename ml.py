import numpy as np
import pandas as pd
import sklearn
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import GradientBoostingClassifier

data = pd.read_csv("phishing.csv")
#droping index column
data = data.drop(['Index'],axis = 1)
# Splitting the dataset into dependant and independant fetature

X = data.drop(["class"],axis =1)
y = data["class"]

# instantiate the model
gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X,y)
# fit the model 
gbc.fit(X_train,Y_train)
gbc_score = gbc.score(X,y)
y_pred = gbc.predict(X_test)
gbc_accuracy = sklearn.metrics.accuracy_score(Y_test, y_pred)
