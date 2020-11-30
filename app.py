import streamlit as st
import pandas as pd 
import numpy 
import urllib.request 
from datetime import datetime 
from datetime import timedelta
import time 

df = pd.read_csv('2020 November General Election - Turnout Rates.csv')
st.title('2020 General Election Turnout')
st.write('Select State')
state = st.selectbox('state',options=df.State.unique())
start_time = st.slider(
"When do you start?",
min_value=datetime(1980, 1, 1),
max_value=datetime(2020, 1, 1),
format="MM/DD/YY")
st.write("Start time:", start_time.strftime("%D"))
if state == 'United States': 
    st.dataframe(data=df)
else: 
    df.loc[df['State']==state]