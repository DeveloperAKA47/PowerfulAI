class Book():
    count = 0
    FILE_NAME = "book.txt"
    def __init__(self,book_name,price=20):
        self.name = book_name
        self.price = price
        if price <= 0:
            self.price = 10
            print("价格必须大于 0")
        Book.count += 1
    def set_price(self,p):
        if p > 0:
            self.price = p
        else:
            print("价格不合法，不修改")
    def save(self):
        with open(Book.FILE_NAME,"a",encoding="utf-8") as f:
            f.write(f"{self.name},{self.price}")
    @classmethod
    def show_total(cls):
        return cls.count
    @staticmethod
    def is_valid_price(p):
        return p > 0
with open(Book.FILE_NAME,"w",encoding="utf-8") as f:
    f.write("")
book1 = Book("西游记",18)
book2 = Book("水浒传",-8)
book1.set_price(-2)
book2.set_price(30)
book1.save()
book2.save()

for book in [book1,book2]:
    print(f"{book.name},{book.price}")

print(Book.count)

with open(Book.FILE_NAME,"r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            print(line)
