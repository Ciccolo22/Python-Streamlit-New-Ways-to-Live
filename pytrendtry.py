
##pytrends



import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import matplotlib
import time

def trend():
    pytrend = TrendReq()
    df = pytrend.trending_searches(pn='united_states')
    df.columns=['topic']
    return df


checkbox = st.checkbox('Click me to find out what is trending on google!!')


if checkbox:
  with st.spinner('Wait for it...'):
    time.sleep(3)
    st.success('Done!')
  st.table(trend())
    


st.sidebar.header(""" 
Trends Prototype volume 1""") 


st.sidebar.write("Need somewhere to find out what is trending in a short amount of time? Try us out")
