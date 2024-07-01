import streamlit as st
from lyricsgenius import Genius
import json
from functions import *

# Initialization will only rereun if fully restarting the app or something changed     
@st.cache_resource
def initialization_function():
    pass
initialization_function()

st.title("Text Input with Confirmation")


import streamlit as st

# Title of the app
st.title("Lyrics Side by Side")

st.write(f"### [hi]")

def display_lyrics(lyric_list):
    for label,lyric in lyric_list:
        # Create a two-column layout
        col1, col2 = st.columns(2)

        # Display lyrics side by side
        with col1:
            st.write(f"**{label}**")
            st.write(lyric)

        with col2:
            st.write(f"**{label}**")
            st.write("translation here")


# Text input widget
song_title = st.text_input("Song title:")
song_artist = st.text_input("Song artist:")


# Button to confirm the input
if st.button("Submit"):
    st.write(f"Searching for {song_title} by {song_artist}")
    # Process the input text when the button is clicked
    lyrics = get_lyrics(song_title,song_artist)
    display_lyrics(split_lyrics(lyrics))

