from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def compute_movie_similarity(user_movie_matrix: pd.DataFrame) -> pd.DataFrame:
    similarity = cosine_similarity(user_movie_matrix.T)

    return pd.DataFrame(
        similarity,
        index=user_movie_matrix.columns,
        columns=user_movie_matrix.columns
    )