
# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import gensim.models.keyedvectors as word2vec
import string
import nltk
from nltk.corpus import stopwords

# Create a function for tokenizer

stemmer = nltk.stem.PorterStemmer()
ENGLISH_STOP_WORDS = stopwords.words('english')

def recipe_tokenizer(sentence):
    # remove punctuation and set to lower case
    for punctuation_mark in string.punctuation:
        sentence = sentence.replace(punctuation_mark,'').lower()

    # split sentence into words
    listofwords = sentence.split(' ')
    listofstemmed_words = []

    # remove stopwords and any tokens that are just empty strings
    for word in listofwords:
        if (not word in ENGLISH_STOP_WORDS) and (word!=''):
            # Stem words
            stemmed_word = stemmer.stem(word)
            listofstemmed_words.append(stemmed_word)

    return listofstemmed_words

# Function to load the combined embeddings and TF-IDF vectorizer model
def load_embeddings_and_vectorizer():
    with open('combined_embeddings.pkl', 'rb') as f:
        combined_embeddings = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return combined_embeddings, vectorizer

# Function for finding recipes
def find_similar_recipes(sampled_data, user_input, num_similar=5):
    combined_embeddings, vectorizer = load_embeddings_and_vectorizer()

    # Process user input
    # Create a DataFrame for user input
    user_data = pd.DataFrame({'text_data': [user_input]})
    user_data['text_data'] = user_data['text_data'].str.lower()

    # Vectorize the user input using the provided vectorizer
    user_vectorized_data = vectorizer.transform(user_data['text_data'])

    # Ensure the number of features in user_vectorized_data matches with combined_embeddings
    num_missing_features = combined_embeddings.shape[1] - user_vectorized_data.shape[1]
    if num_missing_features > 0:
        # Add zero columns to user_vectorized_data to match the number of features
        user_vectorized_data = np.pad(user_vectorized_data.toarray(), ((0, 0), (0, num_missing_features)))

    # Compute cosine similarity with user input
    cosine_sim_matrix = cosine_similarity(user_vectorized_data, combined_embeddings)

    # Retrieve similar recipe indices
    similar_recipes = cosine_sim_matrix[0].argsort()[::-1][:num_similar]

    # Get similar recipe names from food_df
    similar_recipe_names = sampled_data.iloc[similar_recipes]['name'].tolist()

    return similar_recipe_names

# Load data
sampled_data = pd.read_pickle("sampled_data.pkl")

# Define the app title and description
st.title('Recipe Recommender :pancakes:')
st.write("Now we're cooking.")


# User input
user_input = st.text_input('What are you craving?')

if st.button('Get Recommendations'):
    # Get recommendations based on user input
    recommended_recipes = find_similar_recipes(sampled_data, user_input, num_similar=5)
    
    # Get the selected recipes from the sampled_data DataFrame
    selected_recipes = sampled_data.loc[sampled_data['name'].isin(recommended_recipes), ['name', 'description', 'ingredients']]

    # Reset the index of selected_recipes to start from 1
    selected_recipes.reset_index(drop=True, inplace=True)
    selected_recipes.index += 1

    # Display the similar recipes in a table
    st.header('Recommended Recipes')
    st.table(selected_recipes)