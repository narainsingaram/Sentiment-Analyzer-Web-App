import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import math
import streamlit as st

nltk.download('vader_lexicon')
nltk.download('punkt')


def get_sentiment_description(text):
    # Create a new SentimentIntensityAnalyzer object
    sia = SentimentIntensityAnalyzer()

    # Analyze the sentiment of the text
    sentiment = sia.polarity_scores(text)

    # Get the 'compound' score from the sentiment dictionary
    compound_score = sentiment['compound']

    # Initialize an empty list to store the sentiment descriptions
    descriptions = []

    tokens = word_tokenize(text)

    # Check the value of the 'compound' score and add the appropriate descriptions to the list
    if compound_score > 0.5:
        descriptions.append("strongly positive")
    elif compound_score > 0.1:
        descriptions.append("positive")
    elif compound_score > -0.1:
        descriptions.append("neutral")
    elif compound_score > -0.5:
        descriptions.append("negative")
    else:
        descriptions.append("strongly negative")

    # Get the 'neg', 'pos', and 'neu' scores from the sentiment dictionary
    neg_score = sentiment['neg']
    pos_score = sentiment['pos']
    neu_score = sentiment['neu']

    # Check the values of the 'neg', 'pos', and 'neu' scores and add the appropriate descriptions to the list
    if neg_score > pos_score and neg_score > neu_score:
        descriptions.append("more negative than positive or neutral")
    elif pos_score > neg_score and pos_score > neu_score:
        descriptions.append("more positive than negative or neutral")
    elif pos_score > neg_score and pos_score > neu_score:
        descriptions.append("more positive than negative or neutral")
    elif math.isclose(neg_score, pos_score, rel_tol=0.1) and neg_score > neu_score:
        descriptions.append("equally negative and positive, more than neutral")
    elif math.isclose(neg_score, neu_score, rel_tol=0.1) and neg_score > pos_score:
        descriptions.append("equally negative and neutral, more than positive")
    elif math.isclose(pos_score, neu_score, rel_tol=0.1) and pos_score > neg_score:
        descriptions.append("equally negative, positive, and neutral")

    for i in tokens:
        result = sia.polarity_scores(i)
        if result["pos"] != 0:
            descriptions.append(f'''\nThe use of the word **:green[{i}]**
                     caused the sentence to become more **:green[positive ({result['compound']})]**.\n
''')
        elif result["neg"] != 0:
            descriptions.append(f'''\nThe use of the word **:red[{i}]**
                                caused the sentence to become more **:red[negative ({result['compound']})]**.\n

''')

    # Return the list of descriptions as a string
    return " \n".join(descriptions)


# Streamlit User Interface
st.set_page_config(page_title='Sentiment Finder', page_icon = "😀")

with st.spinner('Loading...'):
    time.sleep(0.25)

st.header("Python Sentiment Finder")

txt_box_ipt = st.text_area('Enter a statement below to find its overall sentiment/emotion', height=300)
submit = st.button('Generate')

if submit:
    st.info(get_sentiment_description(txt_box_ipt))
