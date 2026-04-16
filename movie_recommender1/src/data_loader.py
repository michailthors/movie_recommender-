import pandas as pd


def load_movies(path: str) -> pd.DataFrame:
    return pd.read_csv(
        path,
        sep="|",
        encoding="latin-1",
        header=None,
        usecols=[0, 1],
        names=["movieId", "title"]
    )
print(load_movies)

def load_ratings(path: str) -> pd.DataFrame:
    return pd.read_csv(
        path,
        sep="\t",
        header=None,
        names=["userId", "movieId", "rating", "timestamp"]
    )