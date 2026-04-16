import streamlit as st
from src.data_loader import load_movies, load_ratings
from src.recommender import create_user_movie_matrix, recommend_movies
from src.similarity import compute_movie_similarity

@st.cache_data
def load_data():
    movies = load_movies("data/ml-100k/u.item")
    ratings = load_ratings("data/ml-100k/u.data")
    return movies, ratings

@st.cache_data
def build_similarity(ratings):
    user_movie_matrix = create_user_movie_matrix(ratings)
    return compute_movie_similarity(user_movie_matrix)

def main():
    st.title("🎬 Movie Recommender System")
    st.write("Item-Based Collaborative Filtering using Cosine Similarity")

    movies, ratings = load_data()
    similarity_df = build_similarity(ratings)

    movie_input = st.text_input("Enter a movie title:")

    if st.button("Recommend"):
        if movie_input:
            matched_title, recommendations = recommend_movies(
                movie_input,
                movies,
                similarity_df
            )

            if not matched_title:
                st.error("No close match found.")
            else:
                st.success(f"Recommendations for: {matched_title}")

                for i, rec in enumerate(recommendations, 1):
                    st.write(f"{i}. {rec}")
        else:
            st.warning("Please enter a movie title.")

if __name__ == "__main__":
    main()