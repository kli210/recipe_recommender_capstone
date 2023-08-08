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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

This project aims to create an intelligent and personalized recipe recommendation system, catering to users' individual preferences and dietary needs. Leveraging advanced data science techniques like Word2Vec, Word Embeddings Neural Network, TF-IDF, and FunkSVD, the system provides users with enticing and relevant recipe suggestions, inspiring culinary creativity.

<div id="header" align="center">
    <img src="input/Tastyfinds.gif" alt="TastyFinds demo">
</div>

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

1. Run the Jupyter Notebooks outlined in the [Contents](#contents) section to explore different aspects of the project.
2. Use the `app_reciperecs.py` script to deploy the recipe recommendation system using Streamlit.
3. Access the deployed app via the provided URL and start exploring personalized recipe recommendations.

## Roadmap

Future enhancements to the project could include:

- Incorporating user search history and ratings for more personalized recommendations using collaborative filtering (FunkSVD).
- Scraping URLs to link recipes, providing users with convenient access to recipe details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

Kelly Li - kellyli210.kl@gmail.com

Project Link: [https://github.com/kli210/recipe_recommender_capstone](https://github.com/kli210/recipe_recommender_capstone)

### Acknowledgments

I would like to extend my heartfelt gratitude to the following individuals and resources, whose support, guidance, and resources were instrumental in the successful completion of this project:

- BrainStation Instructors & TAs: Thank you for your insightful guidance and continuous support throughout this project.
- Food.com: The invaluable dataset posted on [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=PP_users.csv) served as the foundation of this project.
- Online Communities: The vibrant communities on platforms like Stack Overflow, Reddit, and GitHub, where I found solutions to various challenges.
- Friends and Family: My loved ones who offered encouragement and understanding during the ups and downs of this project.

Your contributions have greatly enriched this project, and I am truly grateful for your involvement.

Happy cooking and happy coding!

<br>

*Cheers,*

*Kelly* c:

