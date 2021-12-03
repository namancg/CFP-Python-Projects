from connect_mysql import get_connection
from dotenv import dotenv_values
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, filename='errors.log', filemode='a')
config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']


def execute_query(query, values=None):
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    """
        to take sql query and execute it
        :param query: query to be executed
        :return: None
     """
    with connection.cursor() as cursor:
        try:
            if not values:
                cursor.execute(query)
            else:
                cursor.execute(query, values)
            connection.commit()
        except Exception as e:
            logging.error(str(e))
            connection.rollback()


def execute_and_get_query(query):
    """
    to take sql query ,execute it and print it
    :param query: query to be executed
    :return: None
    """
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor(buffered=True) as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
            connection.commit()
        except Exception as e:
            logging.error(str(e))
            connection.rollback()


def read_csv_and_insert_to_db(csvfile):
    """
    to read csv and push it to db
    :param csvfile: path of csv file
    :return: None
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
        sql = "insert into books({}) values({})".format(column_values, input_format)
        execute_query(sql, row_values)
