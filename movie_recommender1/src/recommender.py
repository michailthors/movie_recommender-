from rapidfuzz import process
import pandas as pd


def create_user_movie_matrix(ratings: pd.DataFrame) -> pd.DataFrame:
    return ratings.pivot(
        index="userId",
        columns="movieId",
        values="rating"
    ).fillna(0)


def find_movie(title: str, movies_df: pd.DataFrame):
    choices = movies_df["title"].tolist()
    match = process.extractOne(title, choices)

    if match and match[1] > 70:
        return match[0]
    return None


def recommend_movies(movie_title: str,
                     movies: pd.DataFrame,
                     similarity_df: pd.DataFrame,
                     top_n: int = 5):

    matched_title = find_movie(movie_title, movies)

    if not matched_title:
        return None, []

    movie_id = movies[movies["title"] == matched_title]["movieId"].values[0]

    sim_scores = similarity_df[movie_id]
    top_movies = sim_scores.sort_values(ascending=False).iloc[1:top_n+1]

    recommended_titles = movies[
        movies["movieId"].isin(top_movies.index)
    ]["title"].values

    return matched_title, recommended_titles