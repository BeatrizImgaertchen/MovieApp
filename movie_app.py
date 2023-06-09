class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def run(self):
        while True:
            print("1. Add Movie")
            print("2. Delete Movie")
            print("3. Update Movie")
            print("4. List Movies")
            print("5. Generate Website")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "0":
                break
            elif choice == "1":
                self._command_add_movie()
            elif choice == "2":
                self._command_delete_movie()
            elif choice == "3":
                self._command_update_movie()
            elif choice == "4":
                self._command_list_movies()
            elif choice == "5":
                self._command_generate_website()
            else:
                print("Invalid choice. Please try again.")

    def _command_add_movie(self):
        title = input("Enter the movie title: ")
        rating = float(input("Enter the movie rating: "))
        year = int(input("Enter the movie year: "))
        poster = input("Enter the movie poster URL: ")

        self._storage.add_movie(title, rating, year, poster)
        print("Movie added successfully.")

    def _command_delete_movie(self):
        title = input("Enter the movie title: ")
        self._storage.delete_movie(title)
        print("Movie deleted successfully.")

    def _command_update_movie(self):
        title = input("Enter the movie title: ")
        notes = input("Enter the movie notes: ")
        self._storage.update_movie(title, notes)
        print("Movie updated successfully.")

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            for movie in movies:
                print(f"Title: {movie['title']}")
                print(f"Rating: {movie['rating']}")
                print(f"Year: {movie['year']}")
                print(f"Poster: {movie['poster']}")
                print()

    def _command_generate_website(self):
        self._storage.generate_website()
        print("Website generated successfully.")
