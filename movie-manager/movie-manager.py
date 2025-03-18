import sqlite3

connection = sqlite3.connect("movie-database.db")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL
    )
''')



def list_movies():
    print("\n")
    print("*"*70)
    cursor.execute("select * from movies")
    for row in cursor.fetchall():
        print(row)
    print("*"*70)

def add_movie(name,duration):
    cursor.execute("insert into movies (name, duration) values (?,?)", (name , duration))
    connection.commit()
    print("---- Movie added Successfully ----")

def update_movie(id,name ,duration):
    cursor.execute("update movies set name=?, duration=? where id=?", (name,duration,id))
    connection.commit()
    print("---- Movie updated Successfully ----")

def delete_movie(id):
    cursor.execute("delete from movies where id=?", (id,))
    connection.commit()
    print("---- Movie deleted Successfully ----")

def main():
    while True:
        print("\n Movie Manager app with DB")
        print("1. List Movie")
        print("2. Add Movie")
        print("3. Update Movies")
        print("4. Delete Movies")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_movies()
        elif choice == '2':
            name = input("Enter the movie name: ")
            duration = input("Enter movie duration: ")
            add_movie(name,duration)
        elif choice == '3':
            list_movies()
            id = input("Enter the Id of movie you want to edit: ")
            name = input("Enter the movie name: ")
            duration = input("Enter movie duration: ")
            update_movie(id,name,duration)
        elif choice == '4':
            list_movies()
            id = input("Enter the Id of you want to remove: ")
            delete_movie(id)
        elif choice == '5':
            print(" \n --- Thanks for using the App ---")
            break
        else:
            print("Incorrect Choice!")

if __name__ == "__main__":
    main()
