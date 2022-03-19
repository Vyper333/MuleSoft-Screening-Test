#Written by Rea (Vyper333) for MuleSoft Screening Test, Date: 19 March 2022
import sqlite3

conn = sqlite3.connect('mulesoft_proj.db')

#creating cursor
cr = conn.cursor()

#creating the movie table
cr.execute("""CREATE TABLE IF NOT EXISTS movies (
    m_name text,
    lead_actor text,
    lead_actress text,
    director text,
    year_of_release int
)
""")

#creating a list of movie details for the database table 'movies'
movie_list = [
    ('Titanic', 'Leonardo DiCaprio', 'Kate Winslet', 'James Cameron', 1997,),
    ('The Wolf of Wall Street', 'Leonardo DiCaprio', 'Margot Robbie', 'Martin Scorsese', 2014,),
    ('Marley & Me', 'Owen Wilson', 'Jennifer Aniston', 'David Frankel', 2008,),
    ('Revolutionary Road', 'Leonardo DiCaprio', 'Kate Winslet', 'Sam Mendes', 2008,),
    ('Avatar', 'Sam Worthington', 'Zoe Saldaña', 'James Cameron', 2009,),
    ('Murder Mystery', 'Adam Sandler', 'Jennifer Aniston', 'Kyle Newacheck', 2019,),
    ('Orphan', 'Peter Sarsgaard', 'Isabelle Fuhrman', 'Jaume Collet-Serra', 2009,)
]

#inserting the values from the above list into database table 'movies'
cr.executemany("INSERT INTO movies (m_name, lead_actor, lead_actress, director, year_of_release) VALUES(?,?,?,?,?)", movie_list)

#selecting all rows and columns from table 'movies' and printing the same
cr.execute("SELECT rowid, * FROM movies")
print("Printing all rows and columns in table 'movies':\n")
db_movie = cr.fetchall()
for item in db_movie:
    print(item)
print("\n")

#selecting all movies where the lead actor is Leonardo DiCaprio from table 'movies'
cr.execute('SELECT m_name FROM movies WHERE lead_actor ="Leonardo DiCaprio"')
print("Movies starring Leonardo DiCaprio:\n")
actor_movie = cr.fetchall()
for item in actor_movie:
    print(item)
print("\n")

#selecting movie name, director and movie release year from table 'movies' where the name of director starts with letter 'J'
cr.execute('SELECT m_name, director, year_of_release FROM movies WHERE director LIKE "J%"')
print("Movies where Director name begins with letter 'J':\n")
dir_movie = cr.fetchall()
for item in dir_movie:
    print(item)

#Deleting all values from table 'movies'
cr.execute('DELETE FROM movies')

#committing the above commands
conn.commit()

#closing connection
conn.close()