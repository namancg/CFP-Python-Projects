import logging
from connect_mysql import get_connection
import pandas as pd


class functions:
    def __init__(self, USERNAME, PASSWORD, DATABASE):
        try:
            self.connection = get_connection(USERNAME, PASSWORD, DATABASE)
            logging.info("CONNECTED")
            self.cursor = self.connection.cursor()
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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

        except Exception as e:
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
