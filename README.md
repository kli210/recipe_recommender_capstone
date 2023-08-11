# Recipe Recommender System: [TastyFinds](https://kellyli-tastyfinds.streamlit.app/)
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#what-did-i-learn">What Did I Learn?</a></li>
    <li><a href="#challenges-faced">Challenges Faced</a></li>
    <li><a href="#future-directions">Future Directions</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

This project aims to create an intelligent and personalized recipe recommendation system, catering to users' individual preferences and dietary needs. Leveraging advanced data science techniques like Word2Vec, Word Embeddings Neural Network, TF-IDF, and FunkSVD, the system provides users with enticing and relevant recipe suggestions, inspiring culinary creativity.

<br>

<div id="header" align="center">
    <img src="input/Tastyfinds.png" alt="TastyFinds webapp">
</div>

<br>

### Built With

- Python
- Jupyter Notebook
- Scikit-learn
- NumPy
- Pandas
- Surprise
- Streamlit

## Contents

1. [data_preprocessing.ipynb](https://github.com/kli210/recipe_recommender_capstone/blob/main/data_preprocessing.ipynb)
2. [EDA.ipynb](https://github.com/kli210/recipe_recommender_capstone/blob/main/EDA.ipynb)
3. [modelling.ipynb](https://github.com/kli210/recipe_recommender_capstone/blob/main/modelling.ipynb)
4. [advanced_modelling.ipynb](https://github.com/kli210/recipe_recommender_capstone/blob/main/advanced_modelling.ipynb)

## Getting Started

### Prerequisites

- Python (version 3.8 or up)
- Jupyter Notebook
- Git

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/kli210/recipe_recommender_capstone.git
   ```
2. Navigate to the project directory
   ```sh
   cd recipe_recommender_capstone
   ```
3. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Explore how the Recipe Recommender can transform your cooking experience with just a few clicks! Using natural language, you can effortlessly find recipes that match your specific cravings. Watch as the magic happens:

Simply enter your request in everyday language. For example, type in "Japanese soba noodle dishes that are vegetarian."
Witness the power of our recommendation system in action! The web app processes your query, intelligently analyzing the ingredients, descriptions, and more to deliver personalized results.
Instantly receive the top 5 vegetarian dishes that closely align with your request. Say goodbye to tedious searches and hello to a tailored culinary adventure.

<br>

<div id="header" align="center">
    <img src="input/Tastyfinds.gif" alt="TastyFinds demo">
</div>

<br>

Whether you're looking for a quick weeknight meal or aiming to impress with a gourmet creation, this Recipe Recommender is your sous chef in the digital world. Experience the ease of finding recipes that match your cravings and preferences like never before! Try it out [here](https://kellyli-tastyfinds.streamlit.app/).

## What Did I Learn?

Throughout this capstone project, I gained valuable insights into various aspects of data science:

- **Feature Engineering**: I learned the importance of feature engineering in preparing data for modeling. Creating new columns for nutritional values and dietary preferences significantly impacted the model's performance.

- **Dealing with Outliers, Duplicates, and Missing Values**: Managing outliers, duplicates, and missing values was a critical part of data preprocessing. I gained proficiency in handling these challenges effectively to ensure accurate results.

- **Advanced Modeling Techniques**: Implementing techniques like TF-IDF, word embeddings, word2vec, and FunkSVD enhanced my understanding of how these methods improve recommendation systems.

## Challenges Faced

The journey wasn't without challenges:

1. **Data Accessibility and Quality**: Accessing relevant data and dealing with missing information like serving sizes and recipe URLs presented hurdles.

2. **Limited Computational Resources**: Working with large datasets on limited resources required using smaller subsets for local modeling.

## Future Directions

Looking ahead, I have several plans to enhance this project:

- Implement FunkSVD for returning users to personalize recommendations further.
- Incorporate missing parameters like serving sizes and recipe URLs.
- Extend the model with numerical features like nutritional values and recipe complexity.
- Explore collaborative filtering and hybrid models for improved accuracy.
- Deploy the recommendation system on a cloud platform.
- Collaborate with data enthusiasts to expand and refine the project.

## Contributing

Contributions are warmly welcomed! If you have any suggestions, ideas, or improvements that would enhance this project, please don't hesitate to get involved. Feel free to open an issue to discuss your thoughts or submit a pull request with your proposed changes. Your valuable input can help make this project even better.

## Contact

Kelly Li - [kellyli210.kl@gmail.com](mailto:kellyli210.kl@gmail.com)

Project Link: [https://github.com/kli210/recipe_recommender_capstone](https://github.com/kli210/recipe_recommender_capstone)

My personal website: [https://kelly-li.netlify.app/](https://kelly-li.netlify.app/)

### Acknowledgments

I would like to extend my heartfelt gratitude to the following individuals and resources, whose support, guidance, and resources were instrumental in the successful completion of this project:

- **BrainStation Instructors & TAs**: Thank you for your insightful guidance and continuous support throughout this project.
- **Food.com**: The invaluable dataset posted on [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=PP_users.csv) served as the foundation of this project.
- **Online Communities**: The vibrant communities on platforms like Stack Overflow, Reddit, and GitHub, where I found solutions to various challenges.
- **Friends and Family**: My loved ones who offered encouragement and understanding during the ups and downs of this project.

Your contributions have greatly enriched this project, and I am truly grateful for your involvement.

Happy cooking and happy coding!

<br>

*Cheers,*

*Kelly* c:

