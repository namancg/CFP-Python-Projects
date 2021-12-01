import logging
from dotenv import dotenv_values
from fastapi import FastAPI
from model import Book
from mysql_functions import functions
import uvicorn

app = FastAPI()
config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']
mysql_util = functions(USERNAME, PASSWORD, DATABASE)
logging.basicConfig(filename='mysql_errors.log', level=logging.DEBUG)


@app.get("/read_book_data/{id}")
def read_book(id: int):
    query = "select * from books where id={}".format(id)
    result, description = mysql_util.execute_and_fetch_query(query)
    field_names = [i[0] for i in description]
    print_out_record = []
    for row in result:
        out_dictionary = dict(zip(field_names, row))
        print_out_record.append(out_dictionary)
    return print_out_record


@app.put("/add_book_data/")
def create_book(book: Book):
    book_set = (book.id, book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = "insert into books(`id`, `author`, `title`, `image`, `quantity`, `price`, `description`) values(%s,%s,%s,%s,%s,%s,%s)"
    mysql_util.execute_query(query, book_set)
    return {"status": "CREATED"}


@app.put("/update_book_data/{id}")
def update_book(id: int, book: Book):
    book_set = (book.id, book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = "update books set `id` = %s, `author` = %s, `title` = %s, `image` = %s, `quantity` = %s, `price` = %s, " \
            "`description` = %s where id={}".format(id)
    mysql_util.execute_query(query, book_set)
    return {"status": "UPDATED"}


@app.delete('/delete_book_data/{id}')
def delete_book(id: int):
    query = "delete from books where id={}".format(id)
    mysql_util.execute_query(query)
    return {"status": "DELETED"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')
