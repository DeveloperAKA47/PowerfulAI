class Book:
    # 类属性
    count = 0
    FILE_NAME = "book.txt"

    def __init__(self, book_name, price=20):
        self.book_name = book_name
        # 校验价格
        if Book.is_valid_price(price):
            self.price = price
        else:
            self.price = 10
            print(f"价格 {price} 非法，已自动设为默认值 10")
        # 每创建一本书，count +1
        Book.count += 1

    def set_price(self, p):
        if Book.is_valid_price(p):
            self.price = p
        else:
            print(f"价格 {p} 不合法，未进行修改")

    def save(self):
        with open(Book.FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{self.book_name},{self.price}\n")

    @classmethod
    def show_total(cls):
        print(f"一共创建了 {cls.count} 本书")

    @staticmethod
    def is_valid_price(p):
        return p > 0


# ========== 程序执行 ==========

# 1. 清空 book.txt 原有内容
open(Book.FILE_NAME, "w", encoding="utf-8").close()

# 2. 创建 2 本书，其中一本价格为负数（测试校验）
book1 = Book("数学", 65)
book2 = Book("语文", -10)

# 3. 分别修改两本书价格，包含一个非法价格
book1.set_price(80)
book2.set_price(-18)

# 4. 把两本书信息存入文件
book1.save()
book2.save()

# 5. 循环输出每本书书名、价格
for book in [book1, book2]:
    print(f"书名：{book.book_name}，价格：{book.price}")

# 6. 调用类方法输出图书总数量
Book.show_total()

# 7. 读取并打印 book.txt 中所有保存的图书数据
with open(Book.FILE_NAME, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
