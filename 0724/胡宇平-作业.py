from fastapi import FastAPI, File, UploadFile, Query, Path, Body, Form, Response, Header
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    FileResponse,
    StreamingResponse,
    RedirectResponse,
    JSONResponse,
)
from pydantic import BaseModel, Field
import shutil
import os
import csv
import io
import json
import re

books_db = [{"id": 1, "name": "《三体》", "author": "Tom", "money": 9.9}]
app = FastAPI()

""" 路径	请求方法	实现功能
/	GET	欢迎页面
/books	GET	获取所有图书列表
/books/summary	GET	获取图书汇总统计
/books/upload	POST	批量上传图书（支持 CSV / JSON 文件）
/books/download	GET	批量下载图书（支持 JSON / CSV 格式，通过 ?format= 指定）
/books/{book_id}	GET	根据 ID 获取单本图书
/books	POST	添加一本新图书
/books/{book_id}	PUT	根据 ID 更新图书信息
/books/{book_id}	DELETE	根据 ID 删除图书 """


@app.get("/", response_class=HTMLResponse, status_code=200)
def root():
    html = """
    <html>
        <body>
            <h1>欢迎来到图书管理系统</h1>
        </body>
    </html>
    """
    return html


@app.get("/books")
def getBooks():
    return books_db


@app.get("/books/summary")
def getStatics():
    res = {}
    res["total_count"] = 0 if not books_db else len(books_db)
    res["total_money"] = sum([x["money"] for x in books_db])
    res["average_price"] = (
        0 if not books_db else res["total_money"] / res["total_count"]
    )
    res["max_price"] = max([x["money"] for x in books_db])
    res["min_price"] = min([x["money"] for x in books_db])
    return res


@app.post("/books/upload")
async def booksUpload(books: UploadFile = File(...)):
    if books and books.file and re.match(r"\.csv$", books.filename):
        os.makedirs("./tmp", exist_ok=True)
        temppath = os.path.join("./tmp", books.filename)
        with open(temppath, "w", encoding="utf-8") as f:
            shutil.copyfileobj(books.file, f)
        with open(temppath, "r", encoding="utf-8") as f:
            r = csv.DictReader(f)
        count = 0
        for i in r:
            count += 1
            i["id"] = len(books_db) + 1
            books_db.append(i)
        return {"message": f"成功添加 {count} 本图书", "books": books_db}
    elif books and books.file and re.match(r"\.json$", books.filename):
        os.makedirs("./tmp", exist_ok=True)
        temppath = os.path.join("./tmp", books.filename)
        with open(temppath, "w", encoding="utf-8") as f:
            shutil.copyfileobj(books.file, f)
        with open(temppath, "r", encoding="utf-8") as f:
            res = json.load(f)
        if isinstance(res, list):
            count = 0
            for i in res:
                count += 1
                i["id"] = len(books_db) + 1
                books_db.append(i)
            return {"message": f"成功添加 {count} 本图书", "books": books_db}
        elif isinstance(res, dict):
            res["id"] = len(books_db) + 1
            books_db.append(res)
            return {"message": f"成功添加 1 本图书", "books": books_db}

    else:
        return JSONResponse(
            content={"detail": "仅支持 .csv 或 .json 文件"}, status_code=400
        )


@app.get("/books/download")
async def downloadBooks(format: str = Query("csv")):
    def gen():
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=["id", "name", "author", "money"])
        w.writeheader()
        yield buf.getvalue()
        buf.seek(0)
        buf.truncate(0)
        for i in books_db:
            w.writerow(i)
            yield buf.getvalue()
            buf.seek(0)
            buf.truncate(0)

    if format == "csv":
        return StreamingResponse(
            gen(),
            status_code=200,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment;filename=1.csv"},
        )
    elif format == "json":
        return books_db


@app.get("/books/{book_id}")
def getBook(book_id: int = Path(...)):
    res = [x for x in books_db if x["id"] == book_id]
    return (
        JSONResponse(content={"detail": "图书不存在"}, status_code=404)
        if not res
        else JSONResponse(content=res[0])
    )


class Book(BaseModel):
    name: str = Field(...)
    author: str = Field(...)
    money: float = Field(..., ge=0)


@app.post("/books")
def addBook(book: Book):
    res = {
        "id": len(books_db) + 1,
        "author": book.author,
        "name": book.name,
        "money": book.money,
    }
    books_db.append(res)
    return JSONResponse(
        content={
            "message": "添加成功",
            "book": res,
        }
    )


@app.put("/books/{book_id}")
async def updateBook(
    book_id: int = Path(..., ge=0),
    author: str | None = Body(...),
    name: str | None = Body(...),
    money: float | None = Body(..., ge=0),
):
    res = [x for x in books_db if x["id"] == book_id]
    if res:
        if author:
            res[0]["author"] = author
        if name:
            res[0]["name"] = name
        if money is not None:
            res[0]["money"] = money
    return (
        JSONResponse(content={"detail": "图书不存在"}, status_code=404)
        if not res
        else JSONResponse(
            content={
                "message": "更新成功",
                "book": res[0],
            }
        )
    )


@app.delete("/books/{book_id}")
async def delBook(book_id: int = Path(..., ge=0)):
    res = [x for x in books_db if x["id"] == book_id]
    if res:
        for i in books_db:
            if i["id"] == book_id:
                books_db.remove(i)
                break
    return (
        JSONResponse(content={"detail": "图书不存在"}, status_code=404)
        if not res
        else JSONResponse(
            content={
                "message": "删除成功",
                "book": res[0],
            }
        )
    )
