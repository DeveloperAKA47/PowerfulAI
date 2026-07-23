import math
from pprint import pprint
import pandas as pd
from numpy.ma.extras import average
from pandas.core.ops import invalid

#1
def clean_and_analyze_scores(raw_scores: list[object]) -> dict[str, object]:
    b= []
    invalid_count = 0
    if not isinstance(raw_scores, list):
        raise TypeError('raw_scores must be a list')
    for score in raw_scores:
        if isinstance(score, bool):
            invalid_count += 1
            continue
        try:
            score = round(float(score), 1)
        except(ValueError, TypeError):
            invalid_count += 1
            continue
        if math.isnan(score) or math.isinf(score):
            invalid_count += 1
            continue
        if score < 0 or score > 100:
            invalid_count += 1
            continue
        b.append(score)
    if b == []:
        print('ValueError("no valid scores")')
    for i in b:
        ps = 0
        ex = 0
        if i > 60:
            ps += 1
        if i > 90:
            ex += 1
    return {
        "valid_scores": b,
        "count": len(b),
        "total": round(sum(b),2),
        "average": round(sum(b)/len(b), 2),
        "max": max(b),
        "min": min(b),
        "pass_count": ps,
        "excellent_count": ex,
        "invalid_count": invalid_count,
    }
#pprint(clean_and_analyze_scores([1,2,3,90,5,"c"]))
#2
products = [
    {"id": "P001", "name": "键盘", "price": 199.0, "stock": 10},
    {"id": "P002", "name": "鼠标", "price": 89.0, "stock": 25},
    {"id": "P003", "name": "显示器", "price": 1299.0, "stock": 5},
]
def find_product(product: list[dict], product_id: str) -> dict | None:
        for p in products:
            if p["id"] == product_id:
                return p
        else:
            return None

def update_stock(products: list[dict], product_id: str, change: int) -> int:
    for p in products:
        if p["id"] == product_id:
            if p["stock"] < change:
                return "ValueError('stock cannot be negative')"
            else:
                p["stock"] += change
            return p["stock"]
    else:
        return "ValueError('product does not exist')"
def sell_product(products: list[dict], product_id: str, quantity: int) -> float:
    if isinstance(quantity, bool):
        return ("ValueError('quantity must be a positive integer')")
    try:
        score = int(quantity)
    except(ValueError, TypeError):
        return ("ValueError('quantity must be a positive integer')")
    for p in products:
        if p["id"] == product_id:
            if quantity > p["stock"]:
                return "ValueError('insufficient stock')"
            else:
                p["stock"] -= quantity
                return round(p["price"]*quantity,2)
    else:
        return 'ValueError("product does not exist")'
def inventory_value(products: list[dict]) -> float:
    for p in products:
        a = p["stock"] * p["price"]
        print(f"{a}:.2f")
#3
from datetime import datetime
import re
h = True
def parse_log_line(line: str) -> dict[str, object] | None:
    li = line.split("|")
    time_str = li[0].strip()
    li[1] = li[1].replace(" ", "")
    li[2] = li[2].replace(" ", "")
    li[3] = li[3].replace(" ", "")
    li[4] = li[4].replace(" ", "")
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    li[0] = dt
    if li[1] in ("INFO","WARNING","ERROR"):
        fullname = li[2].split("=")
        name =fullname[1]
        d = re.fullmatch(r'[A-Za-z0-9_]+', name)
        if d is not None:
            ac = li[3].split("=")
            act = ac[1]
            e = re.fullmatch(r'[A-Za-z_]+', act)
            if e is not None:
                du = li[4].split("=")
                dura = int(du[1])
                if dura >=0:
                    dic = {
                        "time": li[0],
                        "level": li[1],
                        "user": li[2],
                        "action": li[3],
                        "duration": li[4],
                    }
                    pprint(dic)
    else:
        h = False
        return None
def iter_log_records(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            yield line
            if line == "":
                break
def summarize_logs(file_path: str) -> dict[str, object]:
    pass





