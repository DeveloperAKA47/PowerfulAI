import csv
import datetime
import shutil
from fastapi import FastAPI, Body, Form, UploadFile, File
import os
app = FastAPI()
books_db = [
    {"id":1,"name":"《三体》","author":"Tom","money":9.9}
]
@app.get("/")
def hello():
    return {"welcome"}
@app.get("/books")
def show_all():
    return books_db
@app.get("/books/summary")
def show_summary():
    a = len(books_db)
    return f"共有{a}本书"
@app.get("/books/{1")
def show_book():
    return books_db
@app.get("/books/999")
def show_nbook():
    return "图书不存在"
@app.post("/books")
def create_book(
    name: str = Form(...),
    author: str = Form(...),
    money: float = Form(...)
):
    new_id = books_db[-1]["id"] + 1
    books_db.append({"id": new_id, "name":name,"author": author,"money":money})
    return "添加成功！"
@app.get("/books/1")
def update_book(
    money: float = Form(...),
    author: str = Form(...),
):
    books_db[0]["money"] = money
    books_db[0]["author"] = author
    return "更新成功"
@app.get("/books/999")
def update_nbook(
        money: float = Form(...),
):
    return "图书不存在"
@app.delete("/books/1")
def delete_book():
    books_db.pop()
    return "删除成功"
@app.delete("/books/999")
def delete_nbook():
    return "图书不存在"
@app.post("/books/upload")
def upload_book(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8-sig")
    reader = csv.DictReader(content.splitlines())
    new_id = books_db[-1]["id"] + 1
    for row in reader:
        books_db.append({
            "id": new_id,
            "name": row["name"].strip(),
            "author": row["author"].strip(),
            "money": float(row["money"])
        })
        new_id += 1
    return {"message": "上传成功"}

