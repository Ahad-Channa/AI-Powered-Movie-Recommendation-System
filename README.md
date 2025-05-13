# 🎬 AI-Based Movie Recommendation System

An AI-powered movie recommendation system built using Flask that leverages **hybrid filtering** (collaborative + content-based techniques) to provide personalized movie suggestions. This system also integrates with the **TMDb API** to fetch movie posters and additional metadata, creating a rich user experience.

---

## 🚀 Features

- 🔍 **Hybrid Filtering**: Combines content-based and collaborative filtering.
- 🧠 **Collaborative Filtering**: Uses user-item interactions for personalized recommendations.
- 🧾 **Content-Based Filtering**: Recommends similar movies based on metadata like genre, cast, and crew.
- 🖼️ **Movie Posters**: Fetches high-quality posters using TMDb API.
- 💻 **Web Interface**: Clean and responsive front-end built with Flask and HTML/CSS.
- 📂 **MovieLens Dataset**: Trained on publicly available MovieLens dataset.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Recommendation Logic**: Scikit-learn, Pandas, NumPy, Surprise
- **Frontend**: HTML, CSS, Bootstrap
- **API**: TMDb API (for posters and movie info)
- **Dataset**: [MovieLens Dataset (100k/1M)](https://grouplens.org/datasets/movielens/)

---

## 📦 Installation & Usage

### 🔧 Prerequisites

- Python 3.7+
- pip (Python package manager)
- TMDb API Key (get it from [TMDb](https://www.themoviedb.org/settings/api))

---

### ⚙️ Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
