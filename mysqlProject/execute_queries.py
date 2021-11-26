import logging
from connect_mysql import get_connection
from dotenv import dotenv_values
import pandas as pd
import custom_exception
from queries import create_movies_table_query, create_reviewers_table_query, create_ratings_table_query, \
    reviewers_records, insert_reviewers_query, insert_ratings_query, ratings_records, \
    select_movies_query, select_movies_query_1, select_movies_query_2, select_movies_query_3, select_movies_query_4, \
    select_movies_query_5, delete_table_1, delete_table_3, delete_table_2, show_table_query, insert_movies_query, \
    book_table_creation_query

logging.basicConfig(level=logging.INFO, filename='errors.log')
config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']
book_data = pd.read_csv("book.csv")


class movie:
    def __init__(self, USERNAME, PASSWORD, DATABASE):
        try:
            self.connection = get_connection(USERNAME, PASSWORD, DATABASE)
            logging.info("CONNECTED")
            self.cursor = self.connection.cursor()
        except custom_exception.error as e:
            logging.error(str(e))

    def execute_query(self, query, values=None):
        """
        to execute query
        :param query: query to be executed
        :return:
        """
        try:
            if not values:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, values)
            self.connection.commit()
        except custom_exception.error as e:
            logging.error(str(e))

    def execute_many_query(self, query, values):
        """
        to execute many queries
        :param query: query to be executed
        :param values: values to be used
        :return:
        """

        try:
            self.cursor.executemany(query, values)
            self.connection.commit()
        except custom_exception.error as e:
            logging.error(str(e))
            print(str(e))

    def execute_and_fetch_query(self, query):
        """
        to execute a query and fetch the result from the query
        :param query: query to be executed and fetched
        :return:
        """

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except custom_exception.error as e:
            logging.error(str(e))
            print(str(e))
            self.connection.rollback()
            return None

    def read_csv_and_insert_to_db(self, csvfile):
        """
        to read csv and push it to db
        :param csvfile: path of csv file
        :param table_name: name of the table to be inserted into
        :return:
        """
        rows = []
        column_values = ''
        input_format = ''
        df = pd.read_csv(csvfile)
        columns = df.columns.values.tolist()
        for column in columns:
            column_values += column + ','
            input_format += '%s,'
        column_values = column_values.rsplit(',', 1)[0]
        input_format = input_format.rsplit(',', 1)[0]
        for index, row in df.iterrows():
            row_values = ()
            for column in columns:
                if pd.isna(row[column]):
                    row[column] = 'NULL'
                row_values += (row[column],)
            rows.append(row_values)
            sql = "insert into book_data({}) values({})".format(column_values, input_format)
            self.execute_query(sql, row_values)


if __name__ == "__main__":
    m = movie(USERNAME, PASSWORD, DATABASE)
    m.execute_query(create_movies_table_query)
    m.execute_query(create_reviewers_table_query)
    m.execute_query(create_ratings_table_query)
    result = m.execute_and_fetch_query(show_table_query)
    for row in result:
        print(row)
    m.execute_query(insert_movies_query)
    m.execute_many_query(insert_reviewers_query["query"], reviewers_records["values"])
    m.execute_many_query(insert_ratings_query["query"], ratings_records["values"])
    m.execute_query(select_movies_query)
    m.execute_query(select_movies_query_1)
    m.execute_query(select_movies_query_2)
    m.execute_query(select_movies_query_3)
    m.execute_query(select_movies_query_4)
    m.execute_query(select_movies_query_5)
    m.execute_query(book_table_creation_query)
    m.read_csv_and_insert_to_db("book.csv")
