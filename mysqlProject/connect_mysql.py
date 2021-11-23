from mysql.connector import connect, Error


def get_connection(USERNAME, PASSWORD, DATABASE):
    try:
        connection = connect(
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE,
        )
        print("Connected")
        return connection
    except Error as e:
        print(e)
