import streamlit as st
import pandas as pd 
import numpy 
import urllib.request 
from datetime import datetime 
from datetime import timedelta
import time 

st.title('My first app')
st.write('Below is a table of data for...')
start_time = st.slider(
"When do you start?",
min_value=datetime(1980, 1, 1),
max_value=datetime(2020, 1, 1),
format="MM/DD/YY")
st.write("Start time:", start_time.strftime("%D"))
#pd.read_csv('')