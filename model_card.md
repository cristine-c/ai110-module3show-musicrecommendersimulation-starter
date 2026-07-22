# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

A content-based music recommender that matches songs to a listener's stated taste profile.

---

## 2. Intended Use

VibeMatch generates a ranked list of song recommendations from a small catalog based on how closely each song matches a user's declared preferences (favorite genre, favorite mood, and target values for energy, tempo, valence, danceability, and acousticness).

- **What it generates:** the top *k* songs (default 5) for a given taste profile, each shown with a numeric score and a plain-language list of the reasons it was chosen.
- **Assumptions about the user:** it assumes the user can describe their taste up front as explicit preferences, and that their taste is stable during a session. It does not learn from listening history, skips, or likes.
- **Audience:** this is a **classroom exploration project**, not a production system. It is meant to demonstrate how content-based filtering turns data into ranked predictions, not to serve real listeners at scale.

---

## 3. How the Model Works

Think of every song as having a small "personality card" with a genre label, a mood label, and a handful of dials from 0 to 1 (how energetic it is, how positive it feels, how danceable it is, how acoustic it sounds) plus its tempo in beats per minute. The user fills out the same kind of card describing what they're in the mood for.

To recommend, the model compares each song's card to the user's card and hands out points:

- A big bonus (**+3**) if the genre matches, and a smaller bonus (**+2**) if the mood matches — these are the strongest signals.
- Partial credit for each dial based on **how close** the song's value is to what the user wants. An exact match earns the full points for that dial; the further apart they are, the fewer points, down to zero. Energy is worth up to **+2**, tempo up to **+1.5**, and valence, danceability, and acousticness up to **+1** each.

Every song's points are added into a single score, the songs are sorted from highest to lowest, and the top few are shown along with the specific reasons they scored well.

**Changes from the starter logic:** the starter only returned the first few songs unsorted. I implemented the full scoring recipe, added smooth "closeness" scoring for the numeric features (instead of only exact matches), normalized tempo by a 60-BPM tolerance window so it can be compared fairly against the 0–1 dials, and made the model produce a human-readable reason for every point it awards.

---

## 4. Data

- **Catalog size:** 18 songs stored in `data/songs.csv`.
- **Attributes used per song:** genre and mood (text labels), plus five numeric features — energy, tempo (BPM), valence (musical positivity), danceability, and acousticness. These seven attributes are the only inputs the model scores on.
- **Genres represented:** pop, indie pop, lofi, rock, metal, ambient, jazz, synthwave, hip-hop, classical, edm, country, r&b, reggae, and folk.
- **Moods represented:** happy, chill, intense, moody, relaxed, focused, confident, melancholy, euphoric, nostalgic, romantic, laidback, aggressive, and wistful.
- **Data I added:** the starter file had 10 songs across 7 genres. I added 8 more songs to widen the range of genres and moods (adding hip-hop, classical, edm, country, r&b, reggae, metal, and folk) so the recommender has more diverse material to draw from.
- **What's missing:** the catalog is tiny and each genre has only one or two examples, so it can't capture sub-genres or how tastes blend. There are no lyrics, language, release year, or cultural context — musical taste is far richer than seven numeric dials, and things like nostalgia, lyrical themes, or artist loyalty aren't represented at all.

---

## 5. Strengths

- **Clear-taste users:** it works best for a user with a well-defined profile that exists in the catalog. A "Chill Lofi" user reliably gets the lofi/chill tracks at the top, which matched my intuition.
- **Captures the right patterns:** because numeric closeness is smooth rather than all-or-nothing, songs that are *almost* right (e.g. a pop song in the wrong mood but with matching energy and tempo) still surface, which feels reasonable.
- **Transparent:** every recommendation comes with the exact reasons and points, so it's easy to see *why* a song was chosen — a strength most black-box recommenders lack.
- **Intuitive rankings:** when I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock profiles, the top results in each case were songs I would have picked by hand.

---

## 6. Limitations and Bias

- **Small dataset:** with only 18 songs, the recommender can never do more than reshuffle a tiny pool. Every top-5 list is drawn from the same handful of tracks, so results say as much about what's *available* as about what's a good match.
- **Genre imbalance:** the catalog is unevenly distributed — pop and lofi have several entries while classical, reggae, and folk have only one each. Users who prefer sparsely represented genres get thinner, less satisfying lists, purely because fewer matching songs exist, not because the model understands them worse.
- **Popularity bias (by proxy):** the model has no true popularity signal, but genre imbalance acts as a stand-in for one — the "crowded" genres behave like popular ones and dominate results, while niche genres are effectively buried. A real system trained on play counts would amplify this same effect, repeatedly surfacing already-popular songs.
- **Overfitting to one preference:** because genre (+3) and mood (+2) dominate the score, the system strongly favors songs the user already says they like and rarely surfaces a great song from an unfamiliar genre. Over time this would make recommendations feel repetitive and narrow (a filter bubble).
- **Features it ignores:** no lyrics, language, release date, or listening history, and no awareness of other users' behavior (no collaborative filtering).

---

## 7. Evaluation

- **Profiles tested:** three distinct profiles defined in `src/main.py` — **High-Energy Pop** (pop/happy, high energy & tempo), **Chill Lofi** (lofi/chill, low energy, high acousticness), and **Deep Intense Rock** (rock/intense, fast tempo, low valence).
- **What I looked for:** whether the top result matched the profile's stated genre and mood, whether the numeric dials pushed sensible songs up the list, and whether the reasons shown actually justified the score.
- **What surprised me:** songs from *non-matching* genres sometimes scored surprisingly high when their energy, tempo, and other dials lined up well — showing how much the numeric features matter once the genre/mood bonuses are set aside. It also showed how heavily the +3 genre bonus tilts the results.
- **Simple comparisons:** I ran each profile through the recommender and read the ranked output by hand, checking that the ordering and explanations were consistent with the recipe.

---

## 8. Future Work

- **More and richer data:** grow the catalog and add features like release year, language, and artist so recommendations reflect more of what actually shapes taste.
- **Diversity in the top results:** add a rule that avoids stacking the list with near-identical songs or a single genre, so users get some pleasant surprises instead of only the safest matches.
- **Softer genre/mood weighting:** let users tune how much genre and mood matter, so the system can lean toward discovery instead of always rewarding the familiar.
- **Better explanations:** rank the reasons by how much each contributed, or summarize them in a sentence, so the "why" is even easier to read.
- **Complex tastes:** support multiple favorite genres/moods or weighted preferences so a user isn't forced into a single label.

---

## 9. Personal Reflection

Building this made recommender systems feel much less magical and much more like a transparent set of rules: the model is really just measuring "how close is this song to what you asked for" and adding up points. The most interesting discovery was how much the *weights* shape everything — because genre and mood are worth so much, the system naturally keeps showing you what you already like, which is exactly where filter bubbles come from in real apps. It changed how I think about the music apps I use: when they feel like they "get me," it's often because they're optimizing for similarity to my past behavior, and the flip side of that comfort is that they can quietly stop showing me anything new.
