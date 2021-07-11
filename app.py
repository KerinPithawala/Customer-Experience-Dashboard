from altair.vegalite.v4.api import value
from altair.vegalite.v4.schema.channels import Color
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as pz

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

st.sidebar.markdown("## Display graphs")
select=st.sidebar.selectbox('Vizualization type',['Pie Chart','Histogram'],key= '1')
sentiment_count=data['airline_sentiment'].value_counts()
sentiment_count=pd.DataFrame({'sentiment':sentiment_count.index,'Tweets':sentiment_count.values })

if not st.sidebar.checkbox("Hide",True):
    st.markdown("Number of tweets by sentiment")
    if select=='Histogram':
        fig=pz.bar(sentiment_count,x='Sentiment',y='Tweets',color='Tweets',height= 500 )
        st.plotly_chart(fig)
    else:
        fig=pz.pie(sentiment_count,values='Tweets', names="Sentiment" )
        st.plotly_chart(fig)


