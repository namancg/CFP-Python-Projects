from mysql.connector import connect, Error


def get_connection(USERNAME, PASSWORD, DATABASE):
    """
    function to create and return the connection to database
    :param USERNAME:  username to use in the database
    :param PASSWORD: password for the username
    :param DATABASE: database to be used
    :return:
    """
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