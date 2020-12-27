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
    st.dataframe(data=df.describe())
# If a state is selected show that state 
else: 
    df.loc[df['State']==state]
st.write('Choose a dataset')
dataset = st.selectbox('Dataset', os.listdir('Datasets'))
df2 = pd.read_csv('Datasets/'+dataset)
dataset_string = dataset.replace("_", " ")
st.subheader(dataset_string.replace(".csv","").title() + " Dataset")
st.dataframe(df2)
sns.set_style("whitegrid")
# Other Datasets 

if dataset == "governors_county_candidate.csv": 
    st.dataframe(data=df2.describe())

elif dataset == 'governors_county.csv':
    perdf2 = df2[['percent']]
    perdf2 = perdf2.loc[perdf2['percent'] == 100].count().iloc[0]
    st.write(perdf2,' Counties have had 100 percent of votes counted')
    st.dataframe(df2.describe())
    f = df2.plot()
    st.pyplot(f.figure) 

elif dataset == 'governors_state.csv': 
    f = sns.barplot(x='state',y='votes',data=df2)
    f.set_xticklabels(f.get_xticklabels(), rotation=40, fontsize = 5, ha="right")
    f.set_title('Number of Senate Votes per State')
    st.pyplot(f.figure)
    st.write('Total Votes: ',df2.votes.sum())   

elif dataset == 'house_candidate.csv': 
    st.dataframe(df2.describe()) 
    f = sns.barplot(x='district',y='total_votes',data=df2)
    st.pyplot(f.figure)

elif dataset == 'house_state.csv': 
    st.dataframe(df2.describe())

elif dataset == 'president_county_candidate.csv':   
    st.dataframe(df2.describe())
    f = df2.plot()
    st.pyplot(f.figure)

elif dataset == 'president_county.csv': 
    st.dataframe(df2.describe())
    f = df2.plot()
    st.pyplot(f.figure)

elif dataset == 'senate_state.csv': 
    f = sns.barplot(x='state',y='total_votes',data=df2)
    f.set_xticklabels(f.get_xticklabels(), rotation=40, fontsize = 5, ha="right")
    f.set_title('Number of Senate Votes per State')
    st.pyplot(f.figure)
    st.write('Total Votes: ',df2.total_votes.sum())
