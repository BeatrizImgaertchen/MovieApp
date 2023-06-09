import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        movies = []
        with open(self.file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                movies.append(row)
        return movies

    def add_movie(self, title, year, rating, poster):
        with open(self.file_path, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([title, year, rating, poster])

    def delete_movie(self, title):
        movies = self.list_movies()
        updated_movies = [movie for movie in movies if movie['title'] != title]
        self._save_movies(updated_movies)

    def update_movie(self, title, notes):
        movies = self.list_movies()
        for movie in movies:
            if movie['title'] == title:
                movie['notes'] = notes
                break
        self._save_movies(movies)

    def generate_website(self):
        movies = self.list_movies()

        # Generate the HTML content for the website using the movie data
        website_content = "<html><body>"
        for movie in movies:
            website_content += f"<h1>{movie['title']}</h1>"
            website_content += f"<p>Year: {movie['year']}</p>"
            website_content += f"<p>Rating: {movie['rating']}</p>"
            website_content += f"<img src='{movie['poster']}' alt='Movie Poster'>"
            website_content += "<br><br>"

        website_content += "</body></html>"

        # Save the HTML content to a file
        with open('movies_website.html', 'w') as file:
            file.write(website_content)

        print("Website generated successfully!")

    def _save_movies(self, movies):
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(movies)