import streamlit as st
import pandas as pd
from pycaret.regression import load_model, predict_model
import numpy as np
import seaborn as sns
sns.load_dataset("tips")

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0] 
    return predictions

model = load_model('catboost 2_10_2021')


st.write("""
# Simple Tips Prediction App
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    total_bill = st.sidebar.slider('total_bill', min_value=1, max_value=51, value=1)
    sex = st.selectbox('sex', ['Female', 'Male'])
    smoker = st.selectbox('smoker',['Yes','No'])
    day = st.selectbox('day',['Sun','Sat','Thur','Fri'])
    time = st.selectbox('time',['Dinner','Lunch'])
    size = st.sidebar.slider('size', min_value=1, max_value=6, value=1)
    data = {'total_bill': total_bill,
            'sex': sex,
            'smoker': smoker,
            'day': day,
            'time': time,
            'size':size}
    features = pd.DataFrame([data], index=[0])
    return features

#user will input their features and this is then fed to the model for predictions
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


st.subheader('Predictions')   
predictions = predict(model=model, input_df=df)
st.write('the total estimated tip amount is')
st.write('$',round(predictions,2))

