import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model
import numpy as np

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0] 
    return predictions

model = load_model('penguins_rf')

st.write("""

# Penguin Prediction App

This app is being used to predict a particular species of penguin

""") 


add_selectbox = st.sidebar.selectbox(
"How would you like to make predictions",
("Online", "Batch"))


st.sidebar.header('User input features')

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.sidebar.file_uploader("Upload your csv file", type=['csv'])

if uploaded_file is not None:
  df=pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(input_df)    
    
 

if add_selectbox == 'Online':
    if st.button("Predict"):
        st.success('Prediction')
        prediction=predict(model,input_df=input_df)
        st.write('The species prediction is', prediction)
else:
    if add_selectbox=='Batch':
        if uploaded_file is not None:
            if st.button("Predict"):
                st.success("Predictions")
                predictions=predict_model(estimator=model,data=df)
                st.write(predictions)
