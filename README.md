# 🎬 AI-Powered Movie Recommendation System

An AI-powered movie recommendation system using **React** for the frontend and **Flask** for the backend. It leverages **hybrid filtering** (collaborative + content-based), integrates the **TMDb API** for enhanced movie metadata (e.g., posters, overviews), and delivers intelligent, personalized suggestions.

---

## 🔧 Features

- 🧠 Hybrid Recommendation (Content + Collaborative filtering)
- 🎬 TMDb Integration for movie posters and metadata
- ⚛️ Modern React Frontend with dynamic movie display
- 🐍 Flask Backend API
- 📊 Trained on MovieLens dataset
- 🔍 Search and filter functionality
- 🎨 Clean UI with responsive design

---




## 🚀 Quick Start



### 🔗 Prerequisites

- Python 3.7+
- Node.js + npm
- Git
- TMDb API key ([Get it here](https://www.themoviedb.org/settings/api))

---

### ⚙️ Backend Setup (Flask)

cd backend

## Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

## Install Python dependencies
pip install -r requirements.txt

## Set TMDb API key
echo "TMDB_API_KEY=your_tmdb_key_here" > .env

## Run Flask app
python app.py
---

##Dependencies(install)
pip install -r requirements.txt

---

### 💻 frontend Setup (React)

cd frontend

## Install Node dependencies
npm install

## Run React development server
npm start

##📚 Data Source
This project uses the MovieLens dataset for collaborative filtering training.

---

##📈 Future Improvements
- 🔐 User login/auth system
- ⭐ Rating-based feedback
- 🎥 Trailer previews via YouTube API
-📱 Mobile responsive design enhancements
-🧠 Deep learning-based recommender engine
