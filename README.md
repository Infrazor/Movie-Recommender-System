# 🎬 Movie Recommender System
![GitHub last commit](https://img.shields.io/github/last-commit/Infrazor/movie-recommender-system)
![GitHub repo size](https://img.shields.io/github/repo-size/Infrazor/movie-recommender-system)
![GitHub](https://img.shields.io/github/license/Infrazor/movie-recommender-system)

<p align="center">
  <img src="https://raw.githubusercontent.com/Infrazor/movie-recommender-system/main/assets/banner.png" alt="Movie Recommender Banner" width="100%">
</p>
A content-based movie recommender system built using **Python, Pandas, Scikit-learn**, and **Streamlit**. It suggests similar movies based on text similarity and displays movie posters using the **TMDB API**.

---

## 🚀 Features

- Recommend top 5 similar movies for any selected title
- Integrated with TMDB API for movie posters
- Uses NLP (Bag-of-Words + Cosine Similarity)
- Streamlit web UI with dropdown + images
- Fallback poster for missing movie images

---

## 🧠 How It Works

1. Movie metadata is preprocessed and combined into a single `tags` column.
2. Text is vectorized using `CountVectorizer`.
3. Cosine similarity is calculated to find the most similar movies.
4. The top 5 recommended movies are displayed with poster images via TMDB API.

---

## 🛠️ Tech Stack

- **Python**, **Pandas**, **Scikit-learn**
- **Streamlit** – for frontend web interface
- **TMDB API** – to fetch movie posters
- **Pickle** – to load `movies_dict.pkl` and `similarity.pkl`

---

## 📦 Requirements

Install required packages before running:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
streamlit run app.py
```

Make sure `movies_dict.pkl` and `similarity.pkl` are in the same folder as `app.py`.

---

## 📥 Download similarity.pkl

The `similarity.pkl` file is too large for GitHub (175 MB), so it's hosted on Google Drive:

👉 [Download similarity.pkl from Google Drive](https://drive.google.com/uc?export=download&id=16leZ4tzu5ZMNOtMNWukkYkgG-NAfGpua)

**Steps:**
1. Download the file
2. Place it in your project folder next to `app.py`
3. Run `streamlit run app.py`

> ⚠️ Without this file, recommendations will not work.

---

## 📁 Files in the Project

```
├── app.py               ← Streamlit app
├── movies_dict.pkl      ← Movie metadata
├── similarity.pkl       ← Cosine similarity matrix (external download)
├── requirements.txt     ← List of dependencies
├── README.md            ← You’re reading it!
```

---

## 🙋‍♂️ Author

**Sudhanshu Kumar**  
🔗 [GitHub](https://github.com/Infrazor)  
🔗 [LinkedIn](https://in.linkedin.com/in/sudhanshu-kumar-9a4b37306)

---

⭐ Star this repo if you found it helpful!
