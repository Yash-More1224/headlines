import streamlit as st
from crawl import headlines, sub_headlines, most_watched

st.title("Today's Headlines:\n")

st.header("Main Headlines:")
for i, news in enumerate(headlines):
    st.write(f"{i+1}. {news.text.strip()}")
   
st.header("Smaller Headlines:")
for i, news in enumerate(sub_headlines):
    st.write(f"{i+1}. {news.text.strip()}")

st.header("Most watched:")
for i, news in enumerate(most_watched):
    st.write(f"{i+1}. {news.text.strip()}")