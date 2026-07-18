class Book:
    count = 0
    FILE_NAME = "book.txt"

    def __init__(self, book_name, price=20):
        self.book_name = book_name
        try:
            if price > 0:
                self.price = price
            else:
                self.price = 10
                print("price invalid.set price as 10")
        except Exception:
            print("price invalid.set price as 10")
            self.price = 10
        Book.count += 1

    def set_price(self, p):
        try:
            if p > 0:
                self.price = p
            else:
                print("invalid price.")
                return
        except Exception:
            return print(Exception)

    def save(self):
        with open(Book.FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{self.book_name},{self.price}\n")

    @classmethod
    def show_total(cls):
        print(f"创建书的数量:{cls.count}")

    @staticmethod
    def is_valid_price(p):
        try:
            if p > 0:
                return True
            else:
                return False
        except Exception:
            return False


if __name__ == "__main__":
    with open(Book.FILE_NAME, "w", encoding="utf-8") as f:
        f.write("")
    b1 = Book("1", 1)
    b2 = Book("2", "80")
    b1.set_price(50)
    b2.set_price(-1)
    b1.save()
    b2.save()
    for x in (b1, b2):
        print(f"{x.book_name}:{x.price}")
    Book.show_total()
    with open(Book.FILE_NAME, "r", encoding="utf-8") as f:
        for i in f.readlines():
            print(i.strip())
