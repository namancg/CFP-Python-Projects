from connect_mysql import get_connection
from dotenv import dotenv_values
from queries import create_movies_table_query, create_reviewers_table_query, create_ratings_table_query, \
    reviewers_records, insert_reviewers_query, insert_ratings_query, ratings_records, \
    select_movies_query, select_movies_query_1, select_movies_query_2, select_movies_query_3, select_movies_query_4, \
    select_movies_query_5, delete_table_1, delete_table_3, delete_table_2, show_table_query, insert_movies_query

config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']


def __init__(self, USERNAME, PASSWORD, DATABASE):
    self.connection = get_connection(USERNAME, PASSWORD, DATABASE)
    self.cursor = self.connection.cursor()


def execute_query(self, query):
    """
    to execute query
    :param query: query to be executed
    :return:
    """
    self.cursor.execute(query)
    self.connection.commit()


def execute_many_query(self, query, values):
    """
    to execute many queries
    :param query: query to be executed
    :param values: values to be used
    :return:
    """
    self.cursor.executemany(query, values)
    self.connection.commit()


def execute_and_fetch_query(self, query):
    """
    to execute a query and fetch the result from the query
    :param query: query to be executed and fetched
    :return:
    """
    self.cursor.execute(query)
    result = self.cursor.fetchall()
    self.connection.commit()
    return result


execute_query(create_movies_table_query)
execute_query(create_reviewers_table_query)
execute_query(create_ratings_table_query)
result = execute_and_fetch_query(show_table_query)
for row in result:
    print(row)
execute_query(insert_movies_query)
execute_many_query(insert_reviewers_query, reviewers_records)
execute_many_query(insert_ratings_query, ratings_records)
execute_query(select_movies_query)
execute_query(select_movies_query_1)
execute_query(select_movies_query_2)
execute_query(select_movies_query_3)
execute_query(select_movies_query_4)
execute_query(select_movies_query_5)
