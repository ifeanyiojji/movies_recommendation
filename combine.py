# Import all required libraries
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import pickle
from difflib import get_close_matches

# Set page configuration
st.set_page_config(page_title='Movie Analysis Suite', page_icon='🎬')

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["📊 Data Explorer", "🎥 Movie Recommender"])

# Data Explorer Tab -----------------------------------------------------------
with tab1:
    st.title('📊 Interactive Data Explorer')
    
    # App description
    with st.expander('About this app'):
        st.markdown('**What can this app do?**')
        st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
        st.markdown('**How to use the app?**')
        st.warning('1. Select genres in the dropdown 2. Choose years with the slider. Generates an updated DataFrame and line plot.')

    # Load genre data
    df = pd.read_csv('movies_genres_summary.csv')
    df.year = df.year.astype('int')

    # Widgets
    st.subheader('Which Movie Genre performs ($) best at the box office?')
    genres_list = df.genre.unique()
    genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])
    year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
    year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

    # Data processing
    df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
    reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
    reshaped_df = reshaped_df.sort_values(by='year', ascending=False)

    # Interactive dataframe
    df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
                               column_config={"year": st.column_config.TextColumn("Year")},
                               num_rows="dynamic")

    # Visualization
    df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')
    chart = alt.Chart(df_chart).mark_line(strokeWidth=2.5, opacity=0.8).encode(
        x=alt.X('year:N', title='Year', axis=alt.Axis(grid=True)),
        y=alt.Y('gross:Q', title='Gross earnings ($)', axis=alt.Axis(gridColor='#e0e0e0')),
        color=alt.Color('genre:N', 
                       scale=alt.Scale(range=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3', '#CCB974']),
                       legend=alt.Legend(title='Movie Genre'))
    ).properties(height=400, title='Gross Earnings by Genre Over Time'
    ).configure_view(strokeWidth=0
    ).configure_axis(labelFontSize=12, titleFontSize=14, labelFont='Arial', titleFont='Arial'
    ).configure_title(fontSize=16, font='Arial', anchor='start'
    ).configure_legend(labelFontSize=12, titleFontSize=13, labelFont='Arial', titleFont='Arial')
    
    st.altair_chart(chart, use_container_width=True)

# Movie Recommender Tab -------------------------------------------------------
with tab2:
    st.title('🎥 Movie Recommendation System')
    st.write("Find movies similar to your favorite ones!")

    # Load recommendation data
    with open("model.pkl", "rb") as file:
        model_data = pickle.load(file)
    
    movies_data = model_data['movies_data']
    similarity_matrix = model_data['similarity_matrix']
    titles = movies_data['title'].tolist()

    # Recommendation interface
    movie_name = st.text_input("Enter your favorite movie name:", "").title()
    
    if st.button("Recommend"):
        if movie_name:
            close_matches = get_close_matches(movie_name, titles, n=1, cutoff=0.6)
            if close_matches:
                closest_match = close_matches[0]
                movie_index = movies_data[movies_data['title'] == closest_match].index[0]
                
                similarity_scores = list(enumerate(similarity_matrix[movie_index]))
                sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:11]

                st.subheader(f"Movies similar to '{closest_match}':")
                for i, (index, score) in enumerate(sorted_movies):
                    st.write(f"{i+1}. {movies_data.iloc[index]['title']} ({movies_data.iloc[index]['genres']})")
            else:
                st.error("No close match found! Try another movie.")
        else:
            st.error("Please enter a movie name.")