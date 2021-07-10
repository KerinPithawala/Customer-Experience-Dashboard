import streamlit as st
import pandas as pd
import numpy as np

st.title("customer review of leading us airlines")
st.sidebar.title("customer review of leading us airlines")
st.sidebar.markdown(" sentinment analysis of tweets dashboard")

data_url=("https://raw.githubusercontent.com/KerinPithawala/Customer-Experience-Dashboard/main/Tweets.csv")

@st.cache(persist=True)
def load_data():
    data=pd.read_csv(data_url)
    data['tweet_created']=pd.to_datetime(data['tweet_created'])
    return data
data=load_data()

st.sidebar.subheader('Have a look at a tweet')
random_tweet=st.sidebar.radio('Sentiment',('positive','neutral','negative'))
st.sidebar.markdown(data.query('airline_sentiment== @random_tweet')[['text']].sample(n=1).iat[0,0])
