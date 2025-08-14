
movies = [
    {"title": "Inception", "genre": "Sci-Fi"},
    {"title": "The Godfather", "genre": "Crime"},
    {"title": "The Dark Knight", "genre": "Action"},
    {"title": "Forrest Gump", "genre": "Drama"},
    {"title": "Pulp Fiction", "genre": "Crime"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "The Matrix", "genre": "Sci-Fi"},
    {"title": "Gladiator", "genre": "Action"},
    {"title": "The Lion King", "genre": "Animation"},
]

def recommend_movies_by_genre(movies, preferred_genre):
    """
    Recommends movies from the list based on the user's preferred genre.
    """
    recommendations = [movie["title"] for movie in movies if movie["genre"].lower() == preferred_genre.lower()]
    return recommendations



# Main program
if __name__ == "__main__":
    user_genre = input("Enter your preferred genre: ")
    recommended = recommend_movies_by_genre(movies, user_genre)
    if recommended:
        print(f"Recommended {user_genre} movies: {recommended}")
    else:
        print(f"Sorry, no movies found for the genre '{user_genre}'.")
