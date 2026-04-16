from src.data_loader import load_movies, load_ratings
from src.recommender import create_user_movie_matrix, recommend_movies
from src.similarity import compute_movie_similarity


def main():
    movies = load_movies("data/ml-100k/u.item")
    ratings = load_ratings("data/ml-100k/u.data")

    user_movie_matrix = create_user_movie_matrix(ratings)
    similarity_df = compute_movie_similarity(user_movie_matrix)

    while True:
        movie_input = input("\nEnter a movie title (or 'exit' to quit): ")

        if movie_input.lower() == "exit":
            print("Exiting...")
            break

        matched_title, recommendations = recommend_movies(
            movie_input,
            movies,
            similarity_df
        )

        if not matched_title:
            print("No close match found.")
        else:
            print(f"\nRecommendations for '{matched_title}':")
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")


if __name__ == "__main__":
    main()