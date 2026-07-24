import csv
from typing import List

from fastapi import FastAPI, Path, Body, UploadFile, File
from starlette.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse, Response, \
    StreamingResponse
from pydantic import BaseModel, Field

books_db = [
    {"id":1,"name":"《三体》","author":"Tom","money":9.9}
]

app = FastAPI()

@app.get("/return/html",response_class=HTMLResponse)
def return_html():
    return """
    <html>
        <head><title>图书管理系统</title></head>
        <body>
            <h1>欢迎来到图书管理系统</h1>
            <p>点击 <a href="/docs">这里</a> 查看 API 文档</p>
        </body>
    </html>
    """
# /books	GET	获取所有图书列表
@app.get("/books")
def books():
    return books_db

# 获取图书汇总统计
# /books/summary	GET
@app.get("/books/summary")
def books_summary():
    money = [i["money"] for i in books_db]
    price = [i["price"] for i in books_db]
    return {
        "total_count": len(books_db),
        "total_money": sum(money),
        "average_price": sum(price) / len(price),
        "max_price": max(price),
        "min_price": min(price)
    }

# 获取单本图书（存在）	GET	/books/1
@app.get("/books/{book_id}")
def book(book_id: int =Path(...,ge=1,le=1000)):
    for book in books_db:
        if book["id"] == book_id:
            return book
    return "未找到该书籍"


# /books	POST	添加一本新图书
class InsertBook(BaseModel):
    name: str = Field(...,max_length=5)
    author: str
    money: float
@app.post("/insert")
def insert_book(book:InsertBook):
    new_id=books_db[-1]["id"]+1
    books_db.append({"id":new_id,"name":book.name,"author":book.author,"money":book.money})
    return {
    "message":"添加成功",
    "book":{"id":new_id,"name":book.name,"author":book.author,"money":book.money}
}


# 根据 ID 更新图书信息
class UpdateBook:
    name: str
    author: str
    money: float

@app.put("/update/{book_id}")
def update_book(book_id: int, bk: UpdateBook,is_ok:bool = False):
    if is_ok:
        for book in books_db:
            if book_id == book["id"]:
                book["name"] = bk.name
                book["author"] = bk.author
                book["money"] = bk.money
                return "修改成功"

        return {"detail": "图书不存在"}
    return {"message":"更新成功","book":{"id":book_id,"name":bk.name,"author":bk.author,"money":bk.money}}

# 删除图书
@app.delete("/delete/{book_id}")
def delete_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            books_db.remove(book)
            return {"message":"删除成功","book":book}
    return {"detail": "图书不存在"}

# 批量上传（CSV）
@app.post("/books/upload")
def upload_books(file: UploadFile = File(...)):
    # 判断文件类型
    if not file.filename.endswith(".csv"):
        return {
            "msg": "只能上传CSV文件"
        }
    # 读取文件内容
    content = file.file.read().decode("utf-8")
    # 转换成csv读取对象
    reader = csv.DictReader(content.splitlines())
    count = 0
    for row in reader:
        # 自动生成id
        if books_db:
            new_id = books_db[-1]["id"] + 1
        else:
            new_id = 1
        books_db.append({
            "id": new_id,
            "name": row["name"],
            "author": row["author"],
            "money": float(row["money"])
        })
        count += 1
    return {
        "msg": "上传成功",
        "count": count
    }

# 批量上传（JSON）
@app.post("/books/batch")
def batch_insert(books: List[InsertBook]):

    new_books = []

    start_id = books_db[-1]["id"] + 1 if books_db else 1

    for index, book in enumerate(books):

        new_book = {
            "id": start_id + index,
            "name": book.name,
            "author": book.author,
            "money": book.money
        }

        new_books.append(new_book)

    books_db.extend(new_books)

    return {
        "msg": "批量添加成功",
        "count": len(new_books),
        "data": new_books
    }

# 批量下载（JSON）
@app.get("/books/download")
def download_books():
    books_db = [
        {
            "id": 1,
            "name": "Python",
            "author": "张三",
            "money": 59.9
        },
        {
            "id": 2,
            "name": "FastAPI",
            "author": "李四",
            "money": 69.9
        }
    ]
    return books_db


