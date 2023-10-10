# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


st.link_button("Go to gallery",
               "https://streamlit.io/gallery")
