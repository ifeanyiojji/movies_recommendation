import streamlit as st
import pickle
from difflib import get_close_matches

# Load pre-trained model and data
with open("model.pkl", "rb") as file:
    model_data = pickle.load(file)

# Extract components from the model
movies_data = model_data['movies_data']  # DataFrame with movie details
similarity_matrix = model_data['similarity_matrix']  # Precomputed similarity matrix
titles = movies_data['title'].tolist()  # List of movie titles

# Streamlit app interface
st.title("🎥 Movie Recommendation System")
st.write("Find movies similar to your favorite ones!")

# User input for favorite movie
movie_name = st.text_input("Enter your favorite movie name:", "").title()

# Recommendation logic
if st.button("Recommend"):
    if movie_name:
        # Find close matches for the input movie name
        close_matches = get_close_matches(movie_name, titles, n=1, cutoff=0.6)
        if close_matches:
            closest_match = close_matches[0]
            movie_index = movies_data[movies_data['title'] == closest_match].index[0]
            
            # Get similarity scores for the input movie
            similarity_scores = list(enumerate(similarity_matrix[movie_index]))
            sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:11]  # Top 10

            # Display recommendations
            st.subheader(f"Movies similar to '{closest_match}':")
            for i, (index, score) in enumerate(sorted_movies):
                st.write(f"{i+1}. {movies_data.iloc[index]['title']} ({movies_data.iloc[index]['genres']})")
        else:
            st.error("No close match found! Try another movie.")
    else:
        st.error("Please enter a movie name.")
