import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read the CSV at csv_path and return each song as a dict with numeric fields cast to numbers."""
    numeric_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
    }
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = dict(row)
            song["id"] = int(song["id"])
            for field in numeric_fields:
                song[field] = float(song[field])
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences and return (score, list of reason strings)."""
    score = 0.0
    reasons: List[str] = []

    # +3 if the song's genre matches the user's favorite genre.
    if song["genre"] == user_prefs.get("favorite_genre"):
        score += 3.0
        reasons.append(f"matches favorite genre ({song['genre']})")

    # +2 if the song's mood matches the user's favorite mood.
    if song["mood"] == user_prefs.get("favorite_mood"):
        score += 2.0
        reasons.append(f"matches favorite mood ({song['mood']})")

    # Up to +2 based on how close energy is to the user's target energy.
    # energy is in [0, 1], so closeness = 1 - abs(diff) is also in [0, 1].
    if "target_energy" in user_prefs:
        closeness = 1.0 - abs(song["energy"] - user_prefs["target_energy"])
        points = 2.0 * max(0.0, closeness)
        score += points
        reasons.append(f"energy is a close match (+{points:.2f})")

    # Up to +1.5 based on how close tempo is to the user's target tempo.
    # tempo is in BPM, so normalize the difference by a tolerance window.
    if "target_tempo" in user_prefs:
        TEMPO_TOLERANCE = 60.0  # BPM difference at which closeness reaches 0
        diff = abs(song["tempo_bpm"] - user_prefs["target_tempo"])
        closeness = max(0.0, 1.0 - diff / TEMPO_TOLERANCE)
        points = 1.5 * closeness
        score += points
        reasons.append(f"tempo is a close match (+{points:.2f})")

    # Up to +1 each for valence, danceability, and acousticness similarity.
    for feature in ("valence", "danceability", "acousticness"):
        pref_key = f"target_{feature}"
        if pref_key in user_prefs:
            closeness = 1.0 - abs(song[feature] - user_prefs[pref_key])
            points = 1.0 * max(0.0, closeness)
            score += points
            reasons.append(f"{feature} is a close match (+{points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k as (song, score, explanation) tuples, highest score first."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [
        (song, score, "; ".join(reasons) if reasons else "no strong matches")
        for song, score, reasons in scored[:k]
    ]
