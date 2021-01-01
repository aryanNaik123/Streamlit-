import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import urllib.request 
import os 
# Read Election Turnout File with Pandas
df = pd.read_csv('2020 November General Election - Turnout Rates.csv')
# Setting Seaborn Graph Style 
sns.set_style("whitegrid")
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
# Choose second Dataset to show     
st.write('Choose a dataset')
dataset = st.selectbox('Dataset', os.listdir('Datasets'))
df2 = pd.read_csv('Datasets/'+dataset)
# Display Dataset name correctly 
dataset_string = dataset.replace("_", " ")
st.subheader(dataset_string.replace(".csv","").title() + " Dataset")
# Display Chosen Dataset 
st.dataframe(df2)

# Other Datasets 

# Governor County Candidate Dataset 

if dataset == "governors_county_candidate.csv": 
    st.dataframe(data=df2.describe())

# Governor County Dataset 

elif dataset == 'governors_county.csv':
    perdf2 = df2[['percent']]
    perdf2 = perdf2.loc[perdf2['percent'] == 100].count().iloc[0]
    st.write(perdf2,' Counties have had 100 percent of votes counted')
    st.dataframe(df2.describe())
    f = sns.barplot(x='county',y='total_votes',data=df2.sort_values(by='total_votes', ascending=False).head(10))
    f.set_xticklabels(f.get_xticklabels(), rotation=40, fontsize = 5, ha="right")
    f.set_title('Top 10 Counties by Total Votes')
    st.pyplot(f.figure) 

# Governor State Dataset 

elif dataset == 'governors_state.csv': 
    f = sns.barplot(x='state',y='votes',data=df2)
    f.set_xticklabels(f.get_xticklabels(), rotation=40, fontsize = 5, ha="right")
    f.set_title('Number of Senate Votes per State')
    st.pyplot(f.figure)
    st.write('Total Votes: ',df2.votes.sum())   

# House Candidate Datset 

elif dataset == 'house_candidate.csv': 
    st.subheader('Descriptive Statistics')
    st.dataframe(df2.describe()) 
    st.subheader('Total Votes per Party')
    st.dataframe(df2.groupby('party').aggregate(np.sum))
    f = df2.groupby('party').aggregate(np.sum).plot.bar()
    f.set_title('Total Votes per Party')
    st.pyplot(f.figure)
# House State Dataset 

elif dataset == 'house_state.csv': 
    st.subheader('Descriptive Statistics')
    st.dataframe(df2.describe())

# President County Dataset 

elif dataset == 'president_county_candidate.csv':
    st.subheader('Descriptive Statistics')   
    st.dataframe(df2.describe())
    f = sns.barplot(x='county', y='total_votes', hue='candidate', data=df2)
    st.pyplot(f.figure)

# President County Dataset 

elif dataset == 'president_county.csv': 
    st.dataframe(df2.describe())
    f = sns.barplot(x='county', y='total_votes', data=df2)
    st.pyplot(f.figure)

# Senate State Dataset 

elif dataset == 'senate_state.csv': 
    f = sns.barplot(x='state',y='total_votes',data=df2)
    f.set_xticklabels(f.get_xticklabels(), rotation=40, fontsize = 5, ha="right")
    f.set_title('Number of Senate Votes per State')
    st.pyplot(f.figure)
    st.write('Total Votes: ',df2.total_votes.sum())
