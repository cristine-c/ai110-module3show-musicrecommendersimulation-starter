# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

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
  🎵  TOP RECOMMENDATIONS
============================================================
  Profile: genre=pop, mood=happy, energy=0.8
------------------------------------------------------------

  1. Sunrise City — Neon Echo
     Score: 11.34   [pop · happy]
     Reasons:
       • matches favorite genre (pop)
       • matches favorite mood (happy)
       • energy is a close match (+1.96)
       • tempo is a close match (+1.45)
       • valence is a close match (+0.96)
       • danceability is a close match (+0.99)
       • acousticness is a close match (+0.98)

  2. Gym Hero — Max Pulse
     Score: 8.68   [pop · intense]
     Reasons:
       • matches favorite genre (pop)
       • energy is a close match (+1.74)
       • tempo is a close match (+1.20)
       • valence is a close match (+0.97)
       • danceability is a close match (+0.92)
       • acousticness is a close match (+0.85)

  3. Rooftop Lights — Indigo Parade
     Score: 8.14   [indie pop · happy]
     Reasons:
       • matches favorite mood (happy)
       • energy is a close match (+1.92)
       • tempo is a close match (+1.40)
       • valence is a close match (+0.99)
       • danceability is a close match (+0.98)
       • acousticness is a close match (+0.85)

  4. Night Drive Loop — Neon Echo
     Score: 5.75   [synthwave · moody]
     Reasons:
       • energy is a close match (+1.90)
       • tempo is a close match (+1.25)
       • valence is a close match (+0.69)
       • danceability is a close match (+0.93)
       • acousticness is a close match (+0.98)

  5. Pulse Reactor — Kilohertz
     Score: 5.65   [edm · euphoric]
     Reasons:
       • energy is a close match (+1.68)
       • tempo is a close match (+1.30)
       • valence is a close match (+0.94)
       • danceability is a close match (+0.90)
       • acousticness is a close match (+0.83)

============================================================
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
