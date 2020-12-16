import streamlit as st
import pandas as pd 
import numpy 
import matplotlib.pyplot as plt 
import seaborn as sns 
import urllib.request 
from datetime import datetime 
from datetime import timedelta
import time 
import os 
# Read Election Turnout File with Pandas
df = pd.read_csv('2020 November General Election - Turnout Rates.csv')
# Title the page 
st.title('2020 General Election Turnout')
st.subheader('Select State')
# Select State to display in dataframe
state = st.selectbox('state',options=df.State.unique())
# If US is selected show all states
if state == 'United States': 
    st.dataframe(data=df)
# If a state is selected show that state 
else: 
    df.loc[df['State']==state]
st.write('Choose a dataset')
dataset = st.selectbox('Dataset', os.listdir('Datasets'))
df2 = pd.read_csv('Datasets/'+dataset)
dataset_string = dataset.replace("_", " ")
st.subheader(dataset_string.replace(".csv","").title() + " Dataset")
st.dataframe(df2)
if dataset == 'governors_county.csv':
    perdf2 = df2[['percent']]
    perdf2 = perdf2.loc[perdf2['percent'] == 100].count().iloc[0]
    st.write(perdf2,' Counties have had 100 percent of votes counted')
#    st.write(df2['county'].count())
#    pivot_df2 = pd.pivot_table(df2, index=['county'],values=['total_votes'],aggfunc='sum')
    sns.set_style("whitegrid")
    st.dataframe(df2.describe())
    f = df2.plot()
    st.pyplot(f.figure) 
elif dataset == 'senate_state.csv': 
    st.write('Total Votes: ',df2.total_votes.sum())
elif dataset == 'president_county_candidate.csv':   
    st.dataframe(df2.describe())
    f = df2.plot()
    st.pyplot(f.figure)
