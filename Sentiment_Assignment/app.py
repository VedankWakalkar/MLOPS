import streamlit as st
from textblob import TextBlob

# App title
st.title("Basic Sentiment Analysis App")

# App description
st.write("This application analyzes the sentiment of your input text (positive, negative, or neutral).")

# User input
user_input = st.text_area("Enter your text below:")

# Perform sentiment analysis
if user_input:
    analysis = TextBlob(user_input)
    sentiment = analysis.sentiment.polarity

    # Determine sentiment
    if sentiment > 0:
        st.success("The sentiment is **Positive** 😊")
    elif sentiment < 0:
        st.error("The sentiment is **Negative** 😠")
    else:
        st.info("The sentiment is **Neutral** 😐")
