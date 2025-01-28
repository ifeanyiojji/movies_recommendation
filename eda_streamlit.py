# Import libraries
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

# App description - Explain functionalities in an expander box
with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')

# Question header
st.subheader('Which Movie Genre performs ($) best at the box office?')

# Load data - Read CSV into a Pandas DataFrame
df = pd.read_csv('movies_genres_summary.csv')
df.year = df.year.astype('int')

# Genres selection - Create dropdown menu for genre selection
genres_list = df.genre.unique()
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])

# Year selection - Create slider for year range selection
year_list = df.year.unique()
year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# Subset data - Filter DataFrame based on selections
df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
reshaped_df = reshaped_df.sort_values(by='year', ascending=False)

# Editable DataFrame - Allow users to made live edits to the DataFrame
df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
                            column_config={"year": st.column_config.TextColumn("Year")},
                            num_rows="dynamic")

# Data preparation - Prepare data for charting
df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# Display line chart
# Display line chart with Seaborn-like styling
chart = alt.Chart(df_chart).mark_line(
    strokeWidth=2.5,
    opacity=0.8
).encode(
    x=alt.X('year:N', title='Year', axis=alt.Axis(grid=True)),
    y=alt.Y('gross:Q', title='Gross earnings ($)', axis=alt.Axis(gridColor='#e0e0e0')),
    color=alt.Color('genre:N', 
                   scale=alt.Scale(
                       range=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3', '#CCB974']),
                   legend=alt.Legend(title='Movie Genre')
                  )
).properties(
    height=400,
    title='Gross Earnings by Genre Over Time'
).configure_view(
    strokeWidth=0
).configure_axis(
    labelFontSize=12,
    titleFontSize=14,
    labelFont='Arial',
    titleFont='Arial'
).configure_title(
    fontSize=16,
    font='Arial',
    anchor='start'
).configure_legend(
    labelFontSize=12,
    titleFontSize=13,
    labelFont='Arial',
    titleFont='Arial'
)

st.altair_chart(chart, use_container_width=True)