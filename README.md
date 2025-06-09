# 🎬 Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit. This project uses a dataset of movies to recommend similar films based on genres and user preferences.

---

## 🔍 Overview

This project aims to:
- Recommend movies based on a given title using genre similarity.
- Perform exploratory data analysis (EDA) on the movie dataset.
- Offer an interactive frontend using Streamlit for a smooth user experience.

---

## 🚀 Key Features

- ✅ Content-based filtering using cosine similarity on movie genres.
- ✅ Interactive UI built with Streamlit.
- ✅ Easy-to-use interface: search by movie name and get recommendations instantly.
- ✅ Exploratory Data Analysis (EDA) dashboard for insights into the movie dataset.

---

## 📊 Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn (for vectorization & similarity)
- Streamlit (for UI)
- Matplotlib & Seaborn (for EDA)
- Jupyter Notebook

---

## 🛠️ Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/ifeanyiojji/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
```

## 🚀 Usage
To run the main application:

``` bash
streamlit run app.py
```

To explore the data with EDA:

``` bash
streamlit run eda_streamlit.py
```

To explore both of them 
```bash
streamlit run combine.py
```

### Steps:
1. Launch the app using Streamlit.
2. Enter a movie title in the search box.
3. The system returns a list of top similar movies based on genres.


## 📂 File Structure

movie-recommendation-system/
│
├── app.py                    # Main Streamlit app for movie recommendations
├── combine.py                # Script for combining and preprocessing features
├── eda_streamlit.py          # Streamlit app for Exploratory Data Analysis
├── Movie_Recomendation.ipynb # Development notebook for prototyping
│
├── movies.csv                # Original dataset containing movie details
├── movies_genres_summary.csv # Processed dataset with genre summaries
│
├── requirements.txt          # Python dependencies
├── .gitignore                # Files and folders to be ignored by Git
└── README.md                 # Project documentation



## 👤 Author
Developed by Ifeanyi Ojji

## 📜 License
This project is licensed under the MIT License
