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


# Distinct user preference profiles to try against the catalog.
PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9,
        "target_tempo": 128,
        "target_valence": 0.85,
        "target_danceability": 0.85,
        "target_acousticness": 0.1,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "target_tempo": 75,
        "target_valence": 0.6,
        "target_danceability": 0.55,
        "target_acousticness": 0.8,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "target_tempo": 155,
        "target_valence": 0.4,
        "target_danceability": 0.6,
        "target_acousticness": 0.1,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(name, user_prefs, recommendations)


def print_recommendations(name, user_prefs, recommendations) -> None:
    """Print recommendations in a clean, readable terminal layout."""
    width = 60

    print()
    print("=" * width)
    print(f"  🎵  TOP RECOMMENDATIONS — {name}")
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
