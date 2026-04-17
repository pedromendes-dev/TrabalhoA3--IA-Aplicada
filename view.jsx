import { useEffect, useState } from "react";

function App() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/recommend/1")
      .then(res => res.json())
      .then(data => setMovies(Object.keys(data)));
  }, []);

  return (
    <div>
      <h1>Recomendações</h1>
      <ul>
        {movies.map((movie, index) => (
          <li key={index}>{movie}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
