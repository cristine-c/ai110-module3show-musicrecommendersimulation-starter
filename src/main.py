"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from src.recommender import load_songs, recommend_songs
except ModuleNotFoundError:  # allow running as `python main.py` from src/
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_tempo": 120,
        "target_valence": 0.8,
        "target_danceability": 0.8,
        "target_acousticness": 0.2,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print_recommendations(user_prefs, recommendations)


def print_recommendations(user_prefs, recommendations) -> None:
    """Print recommendations in a clean, readable terminal layout."""
    width = 60

    print()
    print("=" * width)
    print("  🎵  TOP RECOMMENDATIONS")
    print("=" * width)
    print(
        f"  Profile: genre={user_prefs.get('favorite_genre', '-')}, "
        f"mood={user_prefs.get('favorite_mood', '-')}, "
        f"energy={user_prefs.get('target_energy', '-')}"
    )
    print("-" * width)

    if not recommendations:
        print("  No recommendations found.")
        print("=" * width)
        return

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  {rank}. {song['title']} — {song['artist']}")
        print(f"     Score: {score:.2f}   [{song['genre']} · {song['mood']}]")
        print("     Reasons:")
        for reason in explanation.split("; "):
            print(f"       • {reason}")

    print()
    print("=" * width)


if __name__ == "__main__":
    main()
