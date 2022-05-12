import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("5.Shop_rental.csv")
ohe = OneHotEncoder(sparse=False)
data_cat = ohe.fit_transform(data[['station']])
new_data = pd.concat([data.drop(columns=['station']),
                      pd.DataFrame(data_cat,
                                   columns=['station_' + str(col) for col in ohe.categories_[0]])],
                                   axis=1)

joblib.dump(ohe, "/Users/subikim/Desktop/2022Project/ohe_station.pkl")

X = new_data.drop('rental', axis=1)
y = new_data['rental']

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(train_x) # fit( )을 수행하면 min과 max의 범위를 정하게 됩니다.
X_train_transformed = scaler.transform(train_x)

joblib.dump(scaler, "scaler.pkl")

from sklearn.linear_model import LinearRegression
model_scale = LinearRegression()
model_scale.fit(X_train_transformed, train_y)

joblib.dump(model_scale, "model.pkl")




