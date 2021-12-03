import logging
import pathlib
from dotenv import dotenv_values
from fastapi import FastAPI, UploadFile, File
from model import Book
from mysql_functions import read_csv_and_insert_to_db
import uvicorn
from mysql_functions import execute_query, execute_and_get_query

app = FastAPI()
config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']
logging.basicConfig(filename='mysql_errors.log', level=logging.DEBUG)


@app.get("/read_book_data/{id}")
def read_book(id: int):
    query = f"select * from books where id={id}"
    result = execute_and_get_query(query)
    record = dict()
    record["id"] = result[0][0]
    record["author"] = result[0][1]
    record["title"] = result[0][2]
    record["image"] = result[0][3]
    record["quantity"] = result[0][4]
    record["price"] = result[0][5]
    record["description"] = result[0][6]
    return record


@app.post("/add_book_data")
def create_book(book: Book):
    book_set = (book.id, book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = "insert into books(`id`, `author`, `title`, `image`, `quantity`, `price`, `description`) values(%s,%s,%s," \
            "%s,%s,%s,%s) "
    execute_query(query, book_set)
    return {"status": "CREATED"}


@app.put("/update_book_data/{id}")
def update_book(id: int, book: Book):
    book_set = (book.id, book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = f"update books set `id` = %s, `author` = %s, `title` = %s, `image` = %s, `quantity` = %s, `price` = %s, " \
            "`description` = %s where id={}".format(id)
    execute_query(query, book_set)
    return {"status": "UPDATED"}


@app.delete('/delete_book_data/{id}')
def delete_book(id: int):
    query = f"delete from books where id={id}"
    execute_query(query)
    return {"status": "DELETED"}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    file_extension = pathlib.Path(file.filename).suffix
    if file_extension == ".csv":
        read_csv_and_insert_to_db(file.filename)
        return {"filename": file.filename}
    else:
        return {"status": "wrong file type"}
