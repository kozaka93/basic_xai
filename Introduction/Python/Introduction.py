#library
import dalex as dx
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

#apartments dataset from DALEX
#data have 5 numerical variables and 1 categorical variables
data = dx.datasets.load_apartments()
data.head()

#we use one-hot encoding for district variable - get_dummies function from pandas
data = pd.get_dummies(data)
X = data.drop(columns='m2_price')
y = data.m2_price

#we created a random forest model using scikit-learn library
regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X, y)

#we created an explainer with dalex package
exp = dx.Explainer(regr, X, y)

