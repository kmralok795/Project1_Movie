import streamlit as st
from recommender import recommend

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

st.write(
    "Discover movies similar to your favourite movie using **Content-Based Filtering**, **TF-IDF Vectorization**, and **Cosine Similarity**."
)

movie_name = st.text_input(
    "Enter Movie Name"
)

if st.button("Recommend Movies"):

    if movie_name.strip() == "":

        st.warning("Please enter a movie name.")

    else:

        movies = recommend(movie_name)

        if len(movies) == 0:

            st.error("Movie not found.")

        else:

            st.success("Top Recommendations")

            for i, movie in enumerate(movies, start=1):

                st.write(f"**{i}. {movie}**")