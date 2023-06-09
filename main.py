from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson

def main():
    storage_type = input("Enter the storage type (CSV/JSON): ")

    if storage_type.upper() == "CSV":
        storage = StorageCsv('movies.csv')
    elif storage_type.upper() == "JSON":
        storage = StorageJson('movies.json')
    else:
        print("Invalid storage type.")
        return

    movie_app = MovieApp(storage)
    movie_app.run()

if __name__ == "__main__":
    main()
