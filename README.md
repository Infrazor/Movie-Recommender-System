# 🎬 Movie Recommender System

A content-based movie recommender system built using **Python, Pandas, Scikit-learn**, and **Streamlit**. It suggests similar movies based on text similarity and displays movie posters using the **TMDB API**.

---

## 🚀 Features

- Recommend top 5 similar movies for any selected title
- Integrated with TMDB API for movie posters
- Uses NLP (bag-of-words + cosine similarity) for content similarity
- Streamlit-based interactive web UI
- Gracefully handles missing posters with fallback display

---

## 📦 Tech Stack

- **Python**, **Pandas**, **Scikit-learn**
- **Streamlit** for web UI
- **TMDB API** for poster images
- Data preprocessed into `movies_dict.pkl` and `similarity.pkl`

---

## 🧠 How It Works

1. Preprocessed movie metadata and created a `tags` column
2. Converted text to vectors using `CountVectorizer`
3. Calculated similarity with `cosine_similarity`
4. Recommends top 5 similar movies based on user input
5. Poster images fetched via **TMDB API** using movie ID

---

## 🛠️ Installation & Run Locally

```bash
git clone https://github.com/Infrazor/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
