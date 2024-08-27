# Movie Recommendation System

This repository contains a Python-based movie recommendation system that suggests similar movies based on user input. The system leverages a combination of data from Kaggle, Wikipedia, and the TMDB API to provide recommendations.

## Features

- **Movie Data:** Integrates Latest data from English and Hindi movies to create a comprehensive database.
- **Content-Based Filtering:** Recommends movies similar to the user's choice based on cosine similarity of Tags. Tags is the combination of actors, directors & genres.
- **Poster Fetching:** Uses the TMDB API to fetch and display movie posters for recommended movies.
- **Interactive Interface:** Built using Streamlit to allow users to interact with the system and view recommendations in an easy-to-use interface.

## Data Collection

**Kaggle:**
- **English Movies:**
  - **Up to 2016:** Data sourced from [IMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)
  - **For 2017:** Data sourced from [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
- **Hindi Movies:** Data sourced from [Bollywood Movies Dataset](https://www.kaggle.com/datasets/vidhikishorwaghela/bollywood-movies-dataset)

**Wikipedia:**
- **English Movies:** Web scraped data for English movies from 2018 to 2023

**TMDB API:**
- Used to load genres, movie IDs, and crew information where needed



## Installation


To set up and run the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rplkr/movie-recommendation-system.git cd movie-recommendation-system
2. **Install the required packages:**
   ```bash
   pip install streamlit
   pip install scikit-learn
   pip install pandas
   pip install requests
   pip install numpy as np
3. **Extract Files:**
   - Download the `pkl_files.zip` archive from the repository or a provided link.
   - Extract `similarity.pkl` and `movies_dict.pkl` from the `pkl_files.zip` archive into the project directory. These files contain the precomputed similarity scores and movie details required for the recommendation system to function.


4. **Run the Python script:**
   ```bash
   streamlit run app.py

   ```

## Usage


1. **Running the Application:**
   - Launch the Streamlit app by executing the command `streamlit run app.py`.
   - **Select a Movie:** Use the dropdown menu to choose a movie from the list.
   - Click on **'Show Recommendation'** to generate and view the top 5 recommended movies based on your selected movie.

2. **Viewing Recommendations:**
   - The app will display the recommended movies along with their posters.
   - **Posters are dynamically retrieved** using the TMDB API for accurate and up-to-date visuals.

## How It Works

The movie recommendation system works by analyzing the **tags** associated with each movie, **which include genres, cast, and crew details**. Using **vectorization** techniques, it converts these textual tags into numerical vectors. The **cosine similarity** metric is then used to calculate the similarity between movies based on these vectors. This similarity score is used to recommend movies that are most similar to the one selected by the user.

## Recommendation

The recommendation is based on the **cosine similarity** between the selected movie and all other movies in the dataset. It provides a list of the top 5 most similar movies to the one chosen by the user. The system ensures that only movies with relevant similarities are recommended, enhancing the user experience.

## Vectorization

**Count Vectorization** is used to convert the textual movie tags into numerical vectors. Each tag (genre, cast, crew.) is treated as a feature, and the vectorization process creates a matrix where each row represents a movie, and each column represents a specific tag. This matrix is essential for calculating the similarity between movies.

## Cosine Similarity

**Cosine Similarity** is a metric used to measure how similar two movies are based on their tag vectors. It calculates the cosine of the angle between two vectors in a multi-dimensional space, where each dimension corresponds to a tag. A cosine similarity score closer to 1 indicates high similarity, while a score closer to 0 indicates less similarity. The system uses this metric to recommend movies that are closest in similarity to the selected movie.

## Code Structure

The project is organized into the following main components:

- **`app.py`**: The main Streamlit application script. It handles the user interface and interactions, including:
  - **Loading Movie Data:** Loads movie details and similarity scores from pickle files.
  - **User Interface:** Provides a dropdown menu for selecting movies and displays recommended movies and their posters.
  - **Recommendation Logic:** Uses the pre-computed similarity scores to recommend movies similar to the user's selection.
  - **Poster Fetching:** Retrieves movie posters using the TMDB API.

- **`movie_recommendation_system/`**: Directory containing data and additional files.
  - **`pkl_files.zip`**: Contains `movies_dict.pkl` and `similarity.pkl`, which are required for the recommendation system. These files store movie details and similarity scores, respectively.
    - **`movies_dict.pkl`**: Pickle file containing the movie data (titles, tags, etc.) for both English and Hindi movies.
    - **`similarity.pkl`**: Pickle file containing the cosine similarity matrix computed from the movie tags.

  - **`Excel files.zip`**: File containing data on English movies & Hindi movies up to 2023.
    - **`hindi_movies.xlsx`**: Excel file containing data on Hindi movies.
    - **`till 2023.csv`**: CSV file containing data on English movies.


  - **`Jupyter notebooks.zip`**: Jupyter notebooks for data cleaning and preparation, including loading data from CSV and Excel files, handling missing values, and merging datasets.


    - **`movie recommendation final.ipynb`**: Jupyter notebook for developing and testing the movie recommendation algorithm, including vectorization and cosine similarity calculations.


  - Contributions are welcome! Please fork this repository and submit a pull request with your improvements or bug fixes. 

## License

  - This project is licensed under the MIT License - see the LICENSE file for details.
