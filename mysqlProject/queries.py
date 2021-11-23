from mysql.connector import connect, Error
from dotenv import dotenv_values
from getpass import getpass
from connect_mysql import get_connection

config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']
create_movies_table_query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """
create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
create_ratings_table_query = """
        CREATE TABLE ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
show_table_query = "DESCRIBE movies"
alter_table_query = """
 ALTER TABLE movies
 MODIFY COLUMN collection_in_mil DECIMAL(4,1)
 """
insert_movies_query = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama",28.4),
    ("Udaan", 2010, "Drama", 1.5),
    ("Home Alone", 1990, "Comedy", 286.9),
    ("Casablanca", 1942, "Romance", 1.0),
    ("Avengers: Endgame", 2019, "Action", 858.8),
    ("Night of the Living Dead", 1968, "Horror", 2.5),
    ("The Godfather", 1972, "Crime", 135.6),
    ("Haider", 2014, "Action", 4.2),
    ("Inception", 2010, "Adventure", 293.7),
    ("Evil", 2003, "Horror", 1.3),
    ("Toy Story 4", 2019, "Animation", 434.9),
    ("Air Force One", 1997, "Drama", 138.1),
    ("The Dark Knight", 2008, "Action",535.4),
    ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
    ("The Lion King", 1994, "Animation", 423.6),
    ("Pulp Fiction", 1994, "Crime", 108.8),
    ("Kai Po Che", 2013, "Sport", 6.0),
    ("Beasts of No Nation", 2015, "War", 1.4),
    ("Andadhun", 2018, "Thriller", 2.9),
    ("The Silence of the Lambs", 1991, "Crime", 68.2),
    ("Deadpool", 2016, "Action", 363.6),
    ("Drishyam", 2015, "Mystery", 3.0);
"""
insert_reviewers_query = """
INSERT INTO reviewers
(first_name, last_name)
VALUES ( %s, %s );
"""
reviewers_records = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    ("John", "Wayne"),
]
insert_ratings_query = """
INSERT INTO ratings
(rating, movie_id, reviewer_id)
VALUES ( %s, %s, %s)
"""
ratings_records = [
    (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14),
]
select_movies_query = "SELECT * FROM movies LIMIT 5"
select_movies_query_1 = "SELECT title, release_year FROM movies LIMIT 5"
select_movies_query_2 = """
SELECT title, collection_in_mil
FROM movies
WHERE collection_in_mil > 300
ORDER BY collection_in_mil DESC
"""
select_movies_query_3 = """
SELECT CONCAT(title, " (", release_year, ")"),
collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
LIMIT 5
"""
select_movies_query_4 = """
SELECT CONCAT(title, " (", release_year, ")"),
collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
 """
select_movies_query_5 = """
SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
FROM reviewers
INNER JOIN ratings
ON reviewers.id = ratings.reviewer_id
GROUP BY reviewer_id
ORDER BY num DESC
LIMIT 1
"""
delete_table_1 = """DROP TABLE movies ON DELETE CASCADE;"""
delete_table_2 = """DROP TABLE ratings;"""
delete_table_3 = """DROP TABLE reviewers;"""
print("ENTER THE OPERATION TO BE PERFORMED:")
print(
    "1. CREATING TABLES \n2. SHOW TABLE \n3. ALTER TABLE \n4. INSERT INTO TABLES \n5. SELECT QUERIES \n6. DROP ALL "
    "TABLES")
choice = int(input())

if choice == 1:
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor() as cursor:
        cursor.execute(create_movies_table_query)
        cursor.execute(create_reviewers_table_query)
        cursor.execute(create_ratings_table_query)
        print("CREATED TABLES")
        connection.commit()
elif choice == 2:
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor() as cursor:
        cursor.execute(show_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
elif choice == 3:
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor() as cursor:
        cursor.execute(alter_table_query)
        cursor.execute(show_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
elif choice == 4:
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor() as cursor:
        # cursor.execute(insert_movies_query)
        cursor.executemany(insert_reviewers_query, reviewers_records)
        cursor.executemany(insert_ratings_query, ratings_records)
        connection.commit()
        print("INSERTED ELEMENTS")

elif choice == 5:
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor(buffered=True) as cursor:
        cursor.execute(select_movies_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.execute(select_movies_query_1)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.execute(select_movies_query_2)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.execute(select_movies_query_3)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.execute(select_movies_query_4)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.execute(select_movies_query_5)
        result = cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
elif choice == 6:
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor() as cursor:
        cursor.execute(delete_table_1)
        cursor.execute(delete_table_2)
        cursor.execute(delete_table_3)
        connection.commit()
