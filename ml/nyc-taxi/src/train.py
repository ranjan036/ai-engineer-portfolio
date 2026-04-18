import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from src.feature_engineering import clean_data, create_feature

from sklearn.model_selection import train_test_split

import pickle

#load the data
df = pd.read_csv('data/raw/train.csv')
#clean the data 
df = clean_data(df)
# create new /relevant feature 
df = create_feature(df)
df.shape
# Input features
 
Feature_columns = ['trip_distance', 'pickup_hour','is_weekend','pickup_latitude','pickup_longitude','dropoff_latitude','dropoff_longitude']
X = df[Feature_columns]
y = df['trip_duration']

# Split the dataset

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

# Apply standardScaler

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Build the model , we are applying KNN

from sklearn.neighbors import KNeighborsRegressor
knn_model = KNeighborsRegressor(n_neighbors=50)
knn_model.fit(X_train_scaled,y_train)

y_pred = knn_model.predict(X_test_scaled)

from sklearn.metrics import mean_absolute_error

mean_error = mean_absolute_error(y_test, y_pred)
print(mean_error)

#save the model and scaler as pkl file

with open('models/knn_model.pkl', 'wb') as f:
    pickle.dump(knn_model,f)

with open('models/scaler.pkl','wb') as f:
    pickle.dump(scaler,f)    