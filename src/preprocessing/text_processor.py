import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from num2words import num2words
import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

def preprocess_text(text):
    """Preprocess text data"""
    if pd.isna(text):
        return ''
    
    # Convert to string and lowercase
    text = str(text).lower()
    
    # Convert numbers to words
    words = word_tokenize(text)
    processed_words = []
    for word in words:
        if word.isdigit():
            try:
                word = num2words(int(word))
            except:
                pass
        processed_words.append(word)
    text = ' '.join(processed_words)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove stopwords and lemmatize
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return ' '.join(words)

def process_text_column(series):
    """Process text column with TF-IDF"""
    # Apply text preprocessing
    processed_text = series.apply(preprocess_text)
    
    # Calculate max_features based on unique words
    unique_words = set(' '.join(processed_text).split())
    max_features = min(len(unique_words), 100)
    
    # Apply TF-IDF with max_features
    tfidf = TfidfVectorizer(
        max_features=max_features,
        min_df=2,
        max_df=0.95
    )
    text_features = tfidf.fit_transform(processed_text)
    
    # Get feature names for better column labeling
    feature_names = tfidf.get_feature_names_out()
    
    # Convert to DataFrame with meaningful column names
    text_df = pd.DataFrame(
        text_features.toarray(),
        columns=[f'{series.name}_{word}' for word in feature_names],
        index=series.index
    )
    
    # Add information about the transformation
    st.info(f'TF-IDF transformation for column {series.name}:\n'
            f'- Original unique words: {len(unique_words)}\n'
            f'- Selected features: {len(feature_names)}')
    
    return text_df
