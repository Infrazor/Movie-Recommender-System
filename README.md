# 🎬 Movie Recommender System

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io)
[![Deployed on AWS EC2](https://img.shields.io/badge/Deployed-AWS_EC2-green)](http://13.202.218.170:8501)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A content-based movie recommendation engine that suggests similar movies using cosine similarity on NLP tags. It fetches movie posters from the TMDb API and displays them in a dynamic web app using Streamlit.

## 🚀 Demo
**Live**: [Using AWS](http://13.202.218.170:8501)
[Using Render](https://movie-recommender-system-nji5.onrender.com/)
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

The `similarity.pkl` file is too large for GitHub (90 MB), so it's hosted on Google Drive:

👉 [Download similarity.pkl from Google Drive](https://drive.google.com/uc?export=download&id=1Tt908E-ohirYERq2tnykItJDev6Y9F48)

**Steps:**
1. Download the file manually (if needed)
2. Place it in your project folder next to `app.py`
3. Run `streamlit run app.py`

> ⚠️ Without this file, recommendations will not work. If running from the cloud (Render, EC2), the app auto-downloads this file.

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
