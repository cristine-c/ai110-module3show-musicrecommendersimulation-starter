# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version, **VibeMatch 1.0**, is a content-based recommender that matches songs from an 18-song catalog to a listener's stated taste profile. Each song is described by a genre, a mood, and five numeric audio features (energy, tempo, valence, danceability, and acousticness). The user provides the same kind of profile, and the recommender scores every song by how closely it matches, then returns a ranked top-k list where each recommendation is shown with its score and a plain-language explanation of why it was chosen.

---

## How The System Works

Real-world recommendation systems, such as those used by Spotify and YouTube, often combine collaborative filtering and content-based filtering to recommend new content. Collaborative filtering predicts what a user might enjoy by analyzing the listening or viewing behavior of many users with similar preferences. In contrast, content-based filtering recommends items by comparing their attributes, such as genre, mood, energy, and tempo, to the user's past preferences. These systems use both input data (the features of songs or videos) and user data (such as listening history, likes, skips, and watch time) to build a profile of each user's interests. In my recommender, each Song is represented by features including genre, mood, energy, tempo, valence, danceability, and acousticness, while the UserProfile stores the user's preferred values for those features based on songs they have liked. The recommender computes a similarity score for every song by comparing its features with the user's preferences, assigning higher scores to songs that are more similar. Finally, it ranks all songs by their similarity scores and recommends the highest-ranked songs. Unlike Spotify or YouTube, which also use collaborative filtering and large amounts of user behavior data, my recommender uses a content-based filtering approach that prioritizes songs whose characteristics most closely match the user's musical preferences.

This project implements a content-based music recommender. Instead of using the listening behavior of other users, it recommends songs by comparing each song's characteristics to a user's preferred musical features.

#### User Profile

The recommender stores a user profile containing the user's preferred values for the following features:

- Favorite genre
- Favorite mood
- Target energy
- Target tempo
- Target valence
- Target danceability
- Target acousticness

These preferences serve as the reference point when evaluating every song in the dataset.

#### Algorithm Recipe

For each song in `songs.csv`, the recommender starts with a score of 0 and applies the following rules:

- +3 points if the song's genre matches the user's favorite genre.
- +2 points if the song's mood matches the user's favorite mood.
- Up to +2 points based on how close the song's energy is to the user's target energy.
- Up to +1.5 points based on how close the song's tempo is to the user's target tempo.
- Up to +1 point based on valence similarity.
- Up to +1 point based on danceability similarity.
- Up to +1 point based on acousticness similarity.

The similarity for numerical features is calculated by comparing the song's value to the user's preferred value. Songs with values closer to the user's preferences receive higher scores.

After every song has been scored, the recommender sorts the songs from highest score to lowest score and recommends the top-ranked songs.

#### Potential Biases

This recommender is designed to prioritize similarity to the user's existing preferences. Because genre and mood receive the largest weights, the system may favor songs from familiar genres while overlooking songs from different genres that have similar musical qualities. In addition, since the system uses only content-based filtering, it does not consider listening patterns from other users, popularity trends, or opportunities to introduce diverse or unexpected recommendations. As a result, the recommendations may become less varied over time.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
============================================================
  🎵  TOP RECOMMENDATIONS — High-Energy Pop
============================================================
  Profile: genre=pop, mood=happy, energy=0.9
------------------------------------------------------------

  1. Sunrise City — Neon Echo
     Score: 10.94   [pop · happy]
     Reasons:
       • matches favorite genre (pop)
       • matches favorite mood (happy)
       • energy is a close match (+1.84)
       • tempo is a close match (+1.25)
       • valence is a close match (+0.99)
       • danceability is a close match (+0.94)
       • acousticness is a close match (+0.92)

  2. Gym Hero — Max Pulse
     Score: 9.18   [pop · intense]
     Reasons:
       • matches favorite genre (pop)
       • energy is a close match (+1.94)
       • tempo is a close match (+1.40)
       • valence is a close match (+0.92)
       • danceability is a close match (+0.97)
       • acousticness is a close match (+0.95)

  3. Rooftop Lights — Indigo Parade
     Score: 7.80   [indie pop · happy]
     Reasons:
       • matches favorite mood (happy)
       • energy is a close match (+1.72)
       • tempo is a close match (+1.40)
       • valence is a close match (+0.96)
       • danceability is a close match (+0.97)
       • acousticness is a close match (+0.75)

  4. Pulse Reactor — Kilohertz
     Score: 6.15   [edm · euphoric]
     Reasons:
       • energy is a close match (+1.88)
       • tempo is a close match (+1.50)
       • valence is a close match (+0.89)
       • danceability is a close match (+0.95)
       • acousticness is a close match (+0.93)

  5. Storm Runner — Voltline
     Score: 5.32   [rock · intense]
     Reasons:
       • energy is a close match (+1.98)
       • tempo is a close match (+0.90)
       • valence is a close match (+0.63)
       • danceability is a close match (+0.81)
       • acousticness is a close match (+1.00)

============================================================

============================================================
  🎵  TOP RECOMMENDATIONS — Chill Lofi
============================================================
  Profile: genre=lofi, mood=chill, energy=0.35
------------------------------------------------------------

  1. Library Rain — Paper Lanterns
     Score: 11.34   [lofi · chill]
     Reasons:
       • matches favorite genre (lofi)
       • matches favorite mood (chill)
       • energy is a close match (+2.00)
       • tempo is a close match (+1.42)
       • valence is a close match (+1.00)
       • danceability is a close match (+0.97)
       • acousticness is a close match (+0.94)

  2. Midnight Coding — LoRoom
     Score: 11.09   [lofi · chill]
     Reasons:
       • matches favorite genre (lofi)
       • matches favorite mood (chill)
       • energy is a close match (+1.86)
       • tempo is a close match (+1.42)
       • valence is a close match (+0.96)
       • danceability is a close match (+0.93)
       • acousticness is a close match (+0.91)

  3. Focus Flow — LoRoom
     Score: 9.20   [lofi · focused]
     Reasons:
       • matches favorite genre (lofi)
       • energy is a close match (+1.90)
       • tempo is a close match (+1.38)
       • valence is a close match (+0.99)
       • danceability is a close match (+0.95)
       • acousticness is a close match (+0.98)

  4. Spacewalk Thoughts — Orbit Bloom
     Score: 7.67   [ambient · chill]
     Reasons:
       • matches favorite mood (chill)
       • energy is a close match (+1.86)
       • tempo is a close match (+1.12)
       • valence is a close match (+0.95)
       • danceability is a close match (+0.86)
       • acousticness is a close match (+0.88)

  5. Paper Boats — Willow & Wren
     Score: 5.89   [folk · wistful]
     Reasons:
       • energy is a close match (+1.96)
       • tempo is a close match (+1.18)
       • valence is a close match (+0.97)
       • danceability is a close match (+0.90)
       • acousticness is a close match (+0.89)

============================================================

============================================================
  🎵  TOP RECOMMENDATIONS — Deep Intense Rock
============================================================
  Profile: genre=rock, mood=intense, energy=0.95
------------------------------------------------------------

  1. Storm Runner — Voltline
     Score: 11.20   [rock · intense]
     Reasons:
       • matches favorite genre (rock)
       • matches favorite mood (intense)
       • energy is a close match (+1.92)
       • tempo is a close match (+1.42)
       • valence is a close match (+0.92)
       • danceability is a close match (+0.94)
       • acousticness is a close match (+1.00)

  2. Gym Hero — Max Pulse
     Score: 7.18   [pop · intense]
     Reasons:
       • matches favorite mood (intense)
       • energy is a close match (+1.96)
       • tempo is a close match (+0.93)
       • valence is a close match (+0.63)
       • danceability is a close match (+0.72)
       • acousticness is a close match (+0.95)

  3. Iron Verdict — Ashen Crown
     Score: 5.88   [metal · aggressive]
     Reasons:
       • energy is a close match (+1.94)
       • tempo is a close match (+1.18)
       • valence is a close match (+0.91)
       • danceability is a close match (+0.92)
       • acousticness is a close match (+0.94)

  4. Pulse Reactor — Kilohertz
     Score: 5.09   [edm · euphoric]
     Reasons:
       • energy is a close match (+1.98)
       • tempo is a close match (+0.83)
       • valence is a close match (+0.66)
       • danceability is a close match (+0.70)
       • acousticness is a close match (+0.93)

  5. Night Drive Loop — Neon Echo
     Score: 4.64   [synthwave · moody]
     Reasons:
       • energy is a close match (+1.60)
       • tempo is a close match (+0.38)
       • valence is a close match (+0.91)
       • danceability is a close match (+0.87)
       • acousticness is a close match (+0.88)

============================================================
```

The recommendations change significantly depending on the user profile, showing that the recommender responds to different musical preferences. The High-Energy Pop profile recommends upbeat songs with high energy, fast tempos, and mostly pop genres, such as Sunrise City and Gym Hero. The Chill Lofi profile shifts toward slower, lower-energy songs with lofi or ambient characteristics, such as Library Rain and Midnight Coding. The Deep Intense Rock profile prioritizes rock and other high-energy songs with intense moods, placing Storm Runner at the top while still recommending other energetic tracks when they closely match the target energy. These differences demonstrate that the scoring algorithm successfully adjusts recommendations based on the user's preferred genre, mood, and audio features rather than returning the same songs for every profile.

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

- **Changing the genre weight.** With genre worth +3, songs from the user's favorite genre almost always dominated the top of the list. When I mentally lowered it toward the mood weight (+2) or below, songs from other genres with strong numeric matches (energy, tempo, valence) began to surface. This showed how much a single weight controls whether the system rewards familiarity or discovery.

- **Adding the numeric features.** The starter logic only returned the first few songs unsorted. Once I added smooth "closeness" scoring for energy, tempo, valence, danceability, and acousticness, songs that were *almost* right (e.g. a pop song in the wrong mood but with matching energy and tempo) started ranking reasonably instead of being ignored. Normalizing tempo by a 60-BPM tolerance window was important so it could be compared fairly against the 0–1 dials.

- **Different types of users.** I ran three profiles — High-Energy Pop, Chill Lofi, and Deep Intense Rock. Each produced a clearly different top-5, and the top result in every case matched the profile's stated genre and mood. Users whose favorite genre had many catalog entries (pop, lofi) got fuller, more satisfying lists than users pointed at sparse genres (classical, reggae, folk), which exposed the catalog's genre imbalance.

---

## Limitations and Risks

- **Tiny catalog.** With only 18 songs, every top-5 list is drawn from the same small pool, so the results reflect what is *available* as much as what is a genuinely good match.
- **No understanding of lyrics or language.** The model scores only seven attributes (genre, mood, and five audio dials). It has no notion of lyrical themes, language, release year, or cultural context — all things that shape real musical taste.
- **Over-favoring genre and mood.** Because genre (+3) and mood (+2) dominate the score, the system strongly rewards songs the user already likes and rarely surfaces a great song from an unfamiliar genre, which over time creates a filter-bubble effect.
- **Genre imbalance acts as a popularity bias.** Genres with more catalog entries (pop, lofi) dominate results while sparse genres (classical, reggae, folk) are effectively buried — the same dynamic a real system trained on play counts would amplify.
- **No collaborative signal.** It uses only content-based filtering, so it ignores other users' behavior, popularity trends, and any opportunity to introduce diverse or unexpected recommendations.

I go deeper on these in [model_card.md](model_card.md).

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this made recommender systems feel much less magical and much more like a transparent set of rules. The model is really just measuring "how close is this song to what you asked for" and adding up points: text labels earn fixed bonuses, and numeric features earn partial credit that shrinks as the values drift apart. Turning data into a prediction came down to choosing which attributes to compare, how to measure closeness, and how much each one should be worth. Seeing every recommendation come with its exact score and reasons made it clear that a "prediction" here is nothing more than a ranked sum of those design choices.

The most striking thing was how much the *weights* shape everything. Because genre and mood are worth so much, the system naturally keeps showing the user what they already like — which is exactly where bias and filter bubbles come from in real systems. The catalog's genre imbalance made it worse: crowded genres behaved like "popular" ones and dominated, while niche genres were buried, even though the model didn't understand them any less well. It changed how I think about the music apps I use: when they feel like they "get me," it's often because they are optimizing for similarity to my past behavior, and the flip side of that comfort is that they can quietly stop showing me anything new.
