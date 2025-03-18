import sqlite3  # Import the SQLite3 library for database management

# Create or connect to the SQLite database file
connection = sqlite3.connect("movie-database.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
               id INTEGER PRIMARY KEY,   -- Unique ID for each movie
               name TEXT NOT NULL,       -- Movie name (Cannot be NULL)
               duration TEXT NOT NULL    -- Duration of the movie (Cannot be NULL)
    )
''')

# Function to list all movies in the database
def list_movies():
    print("\n")
    print("*" * 70)
    cursor.execute("SELECT * FROM movies")  # Fetch all records from movies table
    for row in cursor.fetchall():  # Iterate through the result set
        print(row)
    print("*" * 70)

# Function to add a new movie to the database
def add_movie(name, duration):
    cursor.execute("INSERT INTO movies (name, duration) VALUES (?, ?)", (name, duration))
    connection.commit()  # Save changes to the database
    print("---- Movie added Successfully ----")

# Function to update movie details in the database
def update_movie(id, name, duration):
    cursor.execute("UPDATE movies SET name=?, duration=? WHERE id=?", (name, duration, id))
    connection.commit()  
    print("---- Movie updated Successfully ----")

# Function to delete a movie from the database
def delete_movie(id):
    cursor.execute("DELETE FROM movies WHERE id=?", (id,))
    connection.commit() 
    print("---- Movie deleted Successfully ----")

# Main function to run the interactive menu
def main():
    while True:
        print("\n Movie Manager App with DB")
        print("1. List Movies")
        print("2. Add Movie")
        print("3. Update Movies")
        print("4. Delete Movies")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_movies()
        elif choice == '2':
            name = input("Enter the movie name: ")
            duration = input("Enter movie duration: ")
            add_movie(name, duration)
        elif choice == '3':
            list_movies() 
            id = input("Enter the ID of the movie you want to edit: ")
            name = input("Enter the new movie name: ")
            duration = input("Enter the new movie duration: ")
            update_movie(id, name, duration)
        elif choice == '4':
            list_movies() 
            id = input("Enter the ID of the movie you want to remove: ")
            delete_movie(id)
        elif choice == '5':
            print("\n --- Thanks for using the App ---")
            break  # Exit the loop and close the app
        else:
            print("Incorrect Choice! Please enter a valid option.")

    connection.close()  # Close the database connection

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()
