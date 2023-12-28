# import package
import pickle
import streamlit as st
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, Lasso, ElasticNet
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
import bz2
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.model_selection import GridSearchCV

# loading model
house_price_predict_model = pickle.load(open('house_price_prediction.sav','rb'))

# Title apps
st.title('Prediksi Harga Rumah')

# input user
col1, col2 = st.columns(2)

LB = col1.number_input(label = 'Masukan Luas Bangunan', min_value=0)
LT = col2.number_input(label = 'Masukan Luas Tanah', min_value=0)
KT = col1.number_input(label = 'Masukan  Jumlah Kamar Tidur', min_value=0)
KM = col2.number_input(label = 'Masukan  Jumlah Kamar Mandi', min_value=0)
GRS = col1.number_input(label = 'Masukan Jumlah Garasi', min_value=0)


# load the train model
with open('house_price_prediction.sav', 'rb') as rf:
    model = pickle.load(rf)

def predict(LB, LT, KT, KM, GRS):
    
    # processing user input
    lists = [LB, LT, KT, KM, GRS]
    
    df = pd.DataFrame(lists).transpose()
    # making predictions using the train model
    prediction = model.predict(df)
    result = int(prediction)
    return result

#prediction
button = st.button('Prediksi')
    
# if button is pressed
if button:
# make prediction
    result = predict(LB, LT, KT, KM, GRS)
    st.success(f'Harga rumahnya sebesar Rp. {result*1000000}')
