from idlelib.run import manage_socket
import shutil
from fastapi import FastAPI,Path, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
import io, csv, json,os
import datetime
# 构建fastapi实例
app = FastAPI()
# 模拟数据库
books_db = [
    {"id":1,"name":"《三体》","author":"Tom","money":9.9}
]
# 欢迎页面
@app.get("/",summary="欢迎页面",status_code=200)
def welcome():
    """
    {"message": "欢迎使用图书管理系统！"}
     """
    return "FastAPI 欢迎您！"
# 查看所有书籍
@app.get("/books",summary="获取所有图书")
def show_all():
    return books_db
# 获取汇总统计
@app.get("/books/summary",summary="获取汇总统计 ",status_code=200)
def show_summary():
    total_count = len(books_db)
    total_money = sum(b.get("money", 0) for b in books_db)
    average_price = total_money / total_count if total_count else 0
    prices = [b.get("money", 0) for b in books_db]
    max_price = max(prices) if prices else 0
    min_price = min(prices) if prices else 0
    return {"total_count": total_count, "total_money": total_money, "average_price": average_price, "max_price": max_price, "min_price": min_price}

# 根据书籍id查询书籍信息
@app.get("/bookname/{name}",summary="根据书籍id查询书籍信息")
def getbookbyname(name: str = Path(...,min_length=1,max_length=3)):
    result = []
    for book in books_db:
        if name in book["name"]:
            result.append(book)
    if result:
        return result
    return "未找到"
# 定义上传书籍信息的模型
class InsertBook(BaseModel):
    title: str = Field(...,max_length=5)
    author: str
# 添加单本图书
@app.post("/insert",summary="添加单本图书")
def insert_book(book: InsertBook):
    # 系统自动生产 id
    new_id = books_db[-1]["id"] + 1
    books_db.append({"id":new_id,"title":book.name,"author":book.author})
    return "添加成功！"
# 更新图书
class UpdateBook(BaseModel):
    name: str = Field(...,max_length=5)
    author: str
# 更新书籍信息
@app.put("/update/{book_id}",summary="更新书籍信息")
def update_book(book_id: int, bk: UpdateBook,is_ok:bool = False):
    if is_ok:
        for book in books_db:
            if book_id == book["id"]:
                book["name"] = bk.name
                book["author"] = bk.author
                return "修改成功"
        return "未找到书籍"
    return "is_ok 查询参数为正确赋值"
# 删除图书
@app.delete("/books/{book_id}", summary="根据 ID 删除图书")
def delete_book(book_id: int):
    for i, b in enumerate(books_db):
        if b["id"] == book_id:
            removed = books_db.pop(i)
            return {"message": "删除成功", "book": removed}
    return "图书不存在"
# 批量上传
@app.post("/books/upload", summary="批量上传图书（CSV/JSON）")
def up_png(id: int,wj : list[UploadFile] = File()):

    # 创建 文件存储路径
    os.makedirs("./uploads", exist_ok=True)


    # 判断书籍是否存在
    ok = [True for bk in books_db if bk["id"] == id]
    if ok:

        for img in wj:
            # 限制上传文件的类型
            if img.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
                return "只允许上传png、jpg、jpeg"
            # 文件重命名
            new_file_name = f"{datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")}_{img.filename}"
            # 拼接目标路径
            file_path = os.path.join("./uploads", new_file_name)
            # 以二进制写入模型大概目标路径
            with open(file_path,"wb") as f:
                # f.write(wj.file.read())  可以写，但不建议。反正文件太大
                # 分块写入
                shutil.copyfileobj(img.file,f)
        return "上传成功"
    return "书籍不存在"