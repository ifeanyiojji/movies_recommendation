# Movie Recommendation System

This project implements a **Movie Recommendation System** using **Content-Based Filtering**. The system recommends movies similar to the one provided by the user based on various features like genres, keywords, tagline, cast, and director.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Difflib

## Project Overview

This movie recommendation system works by calculating the cosine similarity between movies based on their features such as genres, keywords, tagline, cast, and director. After building a feature vector for each movie, the system compares them to suggest similar movies to the user.

## Features

- **Content-based filtering**: Recommends movies based on their similarity to the user’s input movie.
- **Cosine Similarity**: Measures the similarity between the movies using feature vectors.
- **User Input**: Takes user input to find similar movies.

## File Structure

```bash
.
├── movies.csv            # Dataset containing movie information
├── Movie_Recommendation.ipynb     # Python script implementing the recommendation system
└── README.md             # Project documentation



## Requirements
To run this project, you need Python 3.x and the following libraries:

pandas
numpy
scikit-learn

You can install the libraries using pip
"pip install pandas numpy scikit-learn"


## How to Run
1. Download the movies.csv file (or ensure it is in the project folder).
2. Create a jupyter notebook (e.g., Movies_Recommendation.ipynb) and add the following code:
3. Then Run each cell


## Dataset
The dataset used in this project is stored in movies.csv. It contains various movie details, such as:

title (Movie title)
genres (Genres of the movie)
keywords (Keywords associated with the movie)
tagline (Movie tagline)
cast (Main cast of the movie)
director (Director of the movie)

