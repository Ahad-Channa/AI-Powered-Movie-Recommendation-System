# 🎬 AI-Powered Movie Recommendation System

An AI-powered movie recommendation system utilizing **React** for the frontend and **Flask** for the backend. This project leverages **hybrid filtering** (a combination of collaborative and content-based approaches), integrates with the **TMDb API** for rich movie metadata (such as posters and overviews), and aims to deliver intelligent, personalized movie suggestions.

---

## 🔧 Core Features

-   🧠 **Hybrid Recommendation Engine:** Employs both content-based and collaborative filtering techniques for robust and accurate suggestions.
-   🎬 **TMDb API Integration:** Enriches movie data with posters, summaries, ratings, and other metadata from The Movie Database.
-   ⚛️ **Modern React Frontend:** A dynamic and responsive user interface built with React for seamless movie Browse and interaction.
-   🐍 **Flask Backend API:** A lightweight and efficient backend powered by Flask to handle recommendation logic and data serving.
-   📊 **MovieLens Dataset:** Trained on the well-established MovieLens dataset to ensure a solid foundation for collaborative filtering.
-   🔍 **Search and Filtering:** Allows users to easily search for specific movies and filter recommendations based on various criteria.
-   🎨 **Clean and Responsive UI:** Designed with a focus on user experience, featuring a clean interface that adapts to different screen sizes.

---

## 🚀 Getting Started

This section will guide you through setting up the project on your local machine for development and testing purposes.

### 🔗 Prerequisites

Ensure you have the following software installed before proceeding:

-   Python (version 3.7 or higher)
-   Node.js (which includes npm, Node Package Manager)
-   Git (for cloning the repository)
-   A TMDb API Key (You can obtain one by registering at [The Movie Database API Page](https://www.themoviedb.org/settings/api))

---

### ⚙️ Backend Setup (Flask)

Follow these steps to get the Flask backend server running:

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your TMDb API Key:**
    Create a `.env` file in the `backend` directory and add your API key:
    ```
    TMDB_API_KEY='your_tmdb_key_here'
    ```
    Replace `'your_tmdb_key_here'` with your actual TMDb API key.

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The backend server should now be running, typically on `http://127.0.0.1:5000/`.

---

### 💻 Frontend Setup (React)

Follow these steps to get the React frontend development server running:

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```

3.  **Start the React development server:**
    ```bash
    npm start
    ```
    The frontend application should now open in your default web browser, typically at `http://localhost:3000/`.

---

## 📚 Data Source

This project utilizes the **MovieLens dataset** as the primary data source for training the collaborative filtering component of the recommendation engine.

---

## 📈 Future Enhancements

We have several exciting improvements planned for future iterations:

-   🔐 **User Authentication:** Implement a secure login and registration system for personalized user experiences.
-   ⭐ **Rating-Based Feedback:** Allow users to rate movies and incorporate this feedback to refine recommendations.
-   🎥 **Trailer Previews:** Integrate the YouTube API to enable users to watch movie trailers directly within the application.
-   📱 **Enhanced Mobile Responsiveness:** Further optimize the user interface for a seamless experience on mobile devices.
-   🧠 **Advanced Recommender Engine:** Explore and integrate deep learning models for even more sophisticated and nuanced recommendations.

---

## 🤝 Contributing

Contributions are highly welcome! If you have suggestions for improvements or want to fix an issue, please feel free to:

-   Fork the repository.
-   Create a new branch for your feature or bug fix.
-   Submit a pull request with a clear description of your changes.
-   Open an issue to discuss potential changes or report bugs.

We appreciate your help in making this project better!
