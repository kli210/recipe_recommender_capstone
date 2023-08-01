# Project: Recipe Recommender System: TastyFinds

## Description
This project aims to develop a recipe recommender system that provides users with personalized cooking inspirations based on their cravings and available ingredients. The system utilizes data science techniques to analyze a vast collection of recipes and user interactions from Food.com, spanning 18 years.

## Contents

### data_preprocessing.ipynb
This Jupyter notebook outlines the data preprocessing steps undertaken to clean and format the raw dataset. Key actions include converting 'id' columns to strings for ease of manipulation, handling missing values, removing duplicate rows, and extracting relevant information such as nutritional values and dietary preferences.

### EDA.ipynb
The Exploratory Data Analysis (EDA) Jupyter notebook presents insights gained from the preprocessed dataset. This notebook visualizes the distribution of nutritional values, explores correlations between variables, examines user ratings and interactions over time, and identifies popular dietary preferences and ingredients.

### modelling.ipynb
In this Jupyter notebook, we implement the content-based recommendation model, which addresses the "cold start" problem. The model leverages word embeddings for ingredient data and utilizes TF-IDF for text data, enabling us to provide relevant recipe recommendations based on users' preferences.

### advanced_modelling.ipynb
The "advanced_modelling" notebook presents the FunkSVD-based collaborative filtering approach. This model aims to personalize recommendations by incorporating user search history and ratings. It offers an enhanced user experience by suggesting recipes tailored to individual tastes.

## Acknowledgment
This project was developed as part of a data science capstone, and the code and insights presented here are solely for educational purposes. Feel free to explore and adapt the codebase to suit your specific use case or to contribute to the project's development. Happy cooking and happy coding!
