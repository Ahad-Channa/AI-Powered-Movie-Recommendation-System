import React, { useState, useRef } from 'react';
import './App.css';


function App() {
  const [title, setTitle] = useState('');
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');
  const titleRef = useRef(null);

  const fetchRecommendations = async () => {
    try {
      const res = await fetch('http://localhost:5000/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title }),
      });

      const data = await res.json();
      setResults(data);
      setError('');


    } catch (error) {
      console.error('Error fetching recommendations:', error);
      setError('Failed to fetch recommendations. Please check the backend server.');
      setResults([]);
    }
  };

  return (
    <div className="container">
      <h1 ref={titleRef}>🎬 Movie Recommendation System</h1>

      <div className="input-group">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter movie title"
        />
        <button onClick={fetchRecommendations}>Recommend</button>
      </div>

      {error && <p className="error">{error}</p>}

      <ul className="movie-list">
        {results.map((movie, index) => {
          return <li key={index} className="movie-item">
           <img src={movie.poster ? movie.poster : '/notpic.jpg'} alt={movie.title} width="100" />



            <div>
              <strong>{movie.title}</strong> — ⭐ {movie.score}
            </div>
          </li>
})}
      </ul>
    </div>
  );
}

export default App;
