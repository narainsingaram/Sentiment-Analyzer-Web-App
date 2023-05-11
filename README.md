# 😃 Sentiment-Analyzer-Web-App

This program determines the sentiment of a given text input and provides a list of sentiment descriptions. The program uses the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** sentiment analysis tool from the Natural Language Toolkit (nltk) library to analyze the sentiment of the input text.

### **Prerequisites**

Before running the program, you need to install the following dependencies:

- nltk
- streamlit

You can install them using the following command:

```
pip install nltk streamlit
```

You also need to download the VADER lexicon and punkt tokenizer from nltk. You can do this by running the following commands:

```jsx
import nltk

nltk.download('vader_lexicon')
nltk.download('punkt')
```

### **Usage**

To use the program, follow these steps:

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the repository directory.
3. Run the following command to start the program:

```
arduinoCopy code
streamlit run sentiment_finder.py

```

1. Enter a statement in the text box provided and click on the "Generate" button to generate the sentiment description.

### **Code Description**

The **`sentiment_finder.py`** file contains the following functions:

- **`open_css_file(file)`**: Opens a CSS file and applies the styles to the Streamlit app.
- **`get_sentiment_description(text)`**: Analyzes the sentiment of the given text using the VADER sentiment analysis tool and returns a list of sentiment descriptions.
- The Streamlit app UI: Contains a text area for user input and a button to generate the sentiment description.

The program uses the **`SentimentIntensityAnalyzer`** class from the **`nltk.sentiment.vader`** module to analyze the sentiment of the input text. The **`get_sentiment_description`** function then uses the compound, negative, positive, and neutral scores from the analysis to generate a list of sentiment descriptions.

The Streamlit app UI uses the **`text_area`** and **`button`** functions from the **`streamlit`** module to create a text box and a button. The **`st.info`** function is used to display the sentiment description.

### **Conclusion**

This program demonstrates how to use the VADER sentiment analysis tool from the nltk library to analyze the sentiment of a given text input. The program can be easily integrated into a web application or used as a standalone tool to analyze the sentiment of text data.
