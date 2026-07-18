from itertools import count


class Book:
    count=0
    FILE_NAME='book.txt'
    def __init__(self,book_name,price = 20):
        self.book_name=book_name
        if price < 0:
            price=10
            print("价格必须大于0")
        self.price = price
        Book.count += 1
    def save(self):
        with open(self.FILE_NAME,'a',encoding='utf-8') as f:
            f.write(f"{self.book_name},{self.price}\n")
    @classmethod
    def show_total(cls):
        print(f"现在一共创建了{Book.count}本书")
    @staticmethod
    def is_valid_price(p):
        if p<0:
            return False
        else:
            return True
#=============================
with open(Book.FILE_NAME, 'w', encoding='utf-8') as f:
    f.write('')
print("已清空 book.txt")
book1 = Book("a", 35)      # 正常价格
book2 = Book("b", -5)
print("")
book1.book_price = -20
book2.book_price = 12
#==============
for book in (book1, book2):
    print(f"书名：{book.book_name}，价格：{book.price}")
Book.show_total()
with open(Book.FILE_NAME, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:  
            name, price = line.split(',')
            print(f"书名：{name}，价格：{price}")