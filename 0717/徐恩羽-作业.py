# 定义 Book 类
from os import name
class Book:
# 类属性
# count：记录创建图书对象总数量，实例化一本书自动 + 1
# FILE_NAME：固定文件名 book.txt
    count=0
    FILE_NAME= "book.txt"
# 实例属性
# book_name：书名
# price：价格，默认 20
# __init__(book_name, price=20)
# 初始化书名、价格；价格必须大于 0，非法则价格设为 10 并提示；每创建一本图书，count count。
    def __init__(self,book_name,price=20):
        print(f"正在初始化{book_name}{price}")
        self.book_name = book_name
        self.price = price
        if price < 0:
            self.price = 10
            print("价格不合法，已将价格设置为10")
        Book.count += 1
# 实例方法
# set_price(p) 修改价格，校验价格 > 0，不合法不修改并提示。
# save()将当前图书信息追加写入 book.txt，格式：书名,价格，一行一本书。
    def set_price(self, p):
        if p > 0 :
            self.price = p
        else:
            print("价格不合法，修改失败")
    def save(self):
        with open("boox.txt", "a", encoding="utf-8") as f:
            f.write(f"{self.book_name},{self.price}\n")
# 类方法
# show_total()：打印一共创建了多少本书。
    def show_total(self):
        print(Book.count)
# 静态方法
# is_valid_price(p)：判断价格是否大于 0，返回布尔值。
    @staticmethod
    def is_valid_price(p):
        return p>0
# 程序执行步骤
# 先清空 book.txt 原有内容；
with open("boox.txt", "w", encoding="utf-8") as f:
    f.write("")
# 创建 2 本书，其中一本书初始化价格为负数（测试校验）；
book1 = Book("三国",50)
book2 = Book("水浒",-2)
# 分别修改两本书价格，包含一个非法价格；
book1.set_price(20)
print(book1.price)
book2.set_price(-1)
print(book2.price)
# 把两本书信息存入文件；
book1.save()
book2.save()
# 循环输出每本书书名、价格；
for i in [book1, book2]:
    print(i.book_name, i.price)
    # 调用类方法输出图书总数量；
print(Book.count)
# 读取并打印 book.txt 中所有保存的图书数据。
with open("boox.txt", "r", encoding="utf-8") as f:
    print(f.read())