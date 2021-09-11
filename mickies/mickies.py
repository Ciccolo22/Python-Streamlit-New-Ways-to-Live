import streamlit as st
import pandas as pd
import time
data = pd.read_csv('micky.csv', index_col='Item')
Items = data.index
st.sidebar.header("Micky's D's Breakfast Item Comparison App")

name = st.sidebar.text_input('Name Please')

if name:
    st.sidebar.write("Be careful eating too much McDonald's", name)
    time.sleep(1)
    st.sidebar.markdown("*It's later than you think...*")


st.sidebar.subheader("menu item")

item_selection = st.sidebar.selectbox(
"Please select an item",("", Items))


metric_selection = st.sidebar.selectbox(
"Please select a metric",
("","Total Fat", "Cholesterol", "Sodium"))


showframe = st.checkbox('Show example data')


if item_selection:
    if showframe:
        st.table(data.loc[item_selection])
    
    
    
   
  

if metric_selection =="Total Fat":
    st.write("Product Comparison (fat content)")
    st.bar_chart(data.iloc[0:3, 0:1], width=1.3)              
       

if metric_selection =="Cholesterol":
    st.write("Product Comparison (fat content)")
    st.bar_chart(data.iloc[0:3, 1:2], width=1.3)      


  
if metric_selection =="Sodium":
    st.write("Product Comparison (Sodium)")
    st.bar_chart(data.iloc[0:3, 2:], width=1.3)            
