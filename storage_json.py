import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        try:
            with open(self.file_path, 'r') as file:
                movies_data = json.load(file)
            return movies_data
        except FileNotFoundError:
            return []

    def add_movie(self, title, rating, year, poster):
        movie = {"title": title, "rating": rating, "year": year, "poster": poster}
        movies = self.list_movies()
        movies.append(movie)
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        movies = [movie for movie in movies if movie['title'] != title]
        self._save_movies(movies)

    def update_movie(self, title, notes):
        movies = self.list_movies()
        for movie in movies:
            if movie['title'] == title:
                movie['notes'] = notes
                break
        self._save_movies(movies)

    def _save_movies(self, movies):
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=4)

    def generate_website(self):
        movies = self.list_movies()
        if not movies:
            print("No movies found.")
            return

        with open('website.html', 'w') as file:
            file.write("<html>\n")
            file.write("<body>\n")
            file.write("<h1>List of Movies</h1>\n")
            file.write("<ul>\n")
            for movie in movies:
                file.write(f"<li>{movie['title']} - Rating: {movie['rating']} - Year: {movie['year']}</li>\n")
            file.write("</ul>\n")
            file.write("</body>\n")
            file.write("</html>\n")
