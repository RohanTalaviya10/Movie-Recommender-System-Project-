<!DOCTYPE html>
<html>
<head>
    <title>Movie Recommender System</title>
</head>
<body>
    <h1>Movie Recommender System</h1>
    <form action="/" method="post">
        <label for="movie">Select a movie:</label>
        <select id="movie" name="movie">
            {% for movie in movie_list %}
                <option value="{{ movie }}">{{ movie }}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Show Recommendation">
    </form>
    {% if recommended_movie_names %}
        <h2>Recommended Movies:</h2>
        <ul>
            {% for name, poster in zip(recommended_movie_names, recommended_movie_posters) %}
                <li>{{ name }}</li>
                <img src="{{ poster }}" alt="Poster">
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
