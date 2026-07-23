
data = [78, "92", " 65.5 ", None, "", True, "abc", 105, 88]

def clean_and_analyze_scores(
    raw_scores: list[object],
) -> dict[str, object]:
    a=len(raw_scores)
    sc=[]
    for score in raw_scores:
        if score is None:
            continue
        elif score is True or score is False:
            continue
        elif score == "":
            continue
        try:
            sc.append(float(score))
        except ValueError:
            continue
    valid_scores=[score for score in sc if score >=0 and score <= 100 ]
    count = len(valid_scores)
    total = sum(valid_scores)
    mx = max(valid_scores)
    mn = min(valid_scores)
    average=sum(valid_scores)/len(valid_scores)
    c = [score for score in valid_scores if score >= 60 ]
    pass_count=len(c)
    c1= [score for score in valid_scores if score >= 90 ]
    excellent_count=len(c1)
    invalid_count=a-count
    return {
    "valid_scores": valid_scores,
    "合法成绩数量": count,
    "总分": total,
    "平均分": average,
    "最高分": mx,
    "最低分": mn,
    "大于等于60分的人数": pass_count,
    "大于等于90分的人数": excellent_count,
    "非法数据数量": invalid_count,
}
print(clean_and_analyze_scores(data))
import abc
from unittest import result

products = [
    {"id": "P001", "name": "键盘", "price": 199.0, "stock": 10},
    {"id": "P002", "name": "鼠标", "price": 89.0, "stock": 25},
    {"id": "P003", "name": "显示器", "price": 1299.0, "stock": 5},
]

def find_product(products: list[dict], product_id: str) -> dict | None:
    # 根据编号查找商品；
    # 找到时返回原商品字典；
    # 找不到时返回None。
    for p in products:
        if p["id"] == product_id:
            return p
    return None
print(find_product(products, "P001"))
def update_stock(products: list[dict], product_id: str, change: int) -> int:
    # change > 0表示增加库存；
    # change < 0表示减少库存；
    # 商品不存在时抛出：ValueError("stock cannot be negative")
    # 修改成功后返回新库存。
    for p in products:
        if p["id"] == product_id:
            new_stock = p["stock"] + change
            if new_stock < 0:
                raise ValueError("stock cannot be negative")
            p["stock"] = new_stock
            return new_stock
print(update_stock(products, "P001",-5))
print(update_stock(products, "P001",5))
def sell_product(products: list[dict], product_id: str, quantity: int) -> float:
    # quantity必须是正整数且不能是布尔值；否则抛出：
    # ValueError("quantity must be a positive integer")
    # 商品不存在时抛出ValueError("product does not exist")；
    # 库存不足时抛出ValueError("insufficient stock")；
    # 销售成功后扣减库存；
    # 返回销售总金额，保留两位小数。
    for p in products:
        if p["id"] == product_id:
            if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
                raise ValueError("quantity must be a positive integer")
            if p["stock"] < quantity:
                raise ValueError("insufficient stock")
            p["stock"] -= quantity
            total_amount = round(p["price"] * quantity, 2)
            return total_amount
print(sell_product(products, "P001",5))
def inventory_value(products: list[dict]) -> float:
    # 计算全部商品的：价格 × 库存之和，返回结果保留两位小数。
    s=0
    for p in products:
        s=s+p["stock"]*p["price"]
    return round(s, 2)
print(inventory_value(products))


a="""
2026-07-22 15:20:01 | INFO | user=Tom | action=login | duration=125
2026-07-22 15:21:10 | WARNING | user=Jerry | action=query | duration=620
invalid line
2026-07-22 15:22:30|ERROR|user=Tom|action=save_file|duration=800
2026-07-22 15:23:05 | INFO | user=Lucy | action=logout | duration=90
"""
# 时间格式固定为 YYYY-MM-DD HH:MM:SS。
# 等级只能是 INFO、WARNING、ERROR。
# 用户名只能包含英文字母、数字、下划线。
# action 只能包含英文字母和下划线。
# duration 必须是非负整数。
# 字段用 | 分隔，两侧允许多余空格。
# 不符合格式的行返回 None。
sample="2026-07-22 15:20:01 | INFO | user=Tom | action=login | duration=125"
import re
def parse_log_line(line: str) -> dict[str, object] | None:
    result=re.match(r'^\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*\|\s*(INFO|WARNING|ERROR)\s*\|\s*user=([A-Za-z0-9_]+)\s*\|\s*action=([A-Za-z_]+)\s*\|\s*duration=(\d+)\s*$', line)
    if result:
        time, level, user, action, duration = result.groups()
        return {
            "time": time,
            "level": level,
            "user": user,
            "action": action,
            "duration": int(duration),
        }
    return None
print(parse_log_line(sample))
# parse_log_line() 返回：
# {
#     "time": "2026-07-22 15:20:01",
#     "level": "INFO",
#     "user": "Tom",
#     "action": "login",
#     "duration": 125,
# }

def iter_log_records(file_path: str):
    ...
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            record = parse_log_line(line)
            if record is not None:
                yield record
print(iter_log_records(a))
    # 每次只处理一行，内存中只有一行
# iter_log_records() 要求：
# 使用生成器；
# 逐行读取；
# 只 yield 合法记录；
# 不允许使用 readlines()。

def summarize_logs(file_path: str) -> dict[str, object]:
    ...
    
    
# summarize_logs() 返回：
# {
#     "valid_count": 合法日志数量,
#     "level_counts": {
#         "INFO": 数量,
#         "WARNING": 数量,
#         "ERROR": 数量,
#     },
#     "average_duration": 平均耗时,
#     "slow_users": [...],
# }





class BatchIterator:
    def __init__(
        self,
        data,
        batch_size: int,
        *,
        drop_last: bool = False,
    ):
        if (
            not isinstance(batch_size, int)
            or isinstance(batch_size, bool)
            or batch_size <= 0
        ):
            raise ValueError("batch_size must be a positive integer")

        self.data = list(data)
        self.batch_size = batch_size
        self.drop_last = drop_last
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        # 已经遍历结束
        if self.index >= len(self.data):
            raise StopIteration

        # 当前批次
        batch = self.data[
            self.index:self.index + self.batch_size
        ]

        # 移动指针
        self.index += self.batch_size


        # 最后一批不足 batch_size
        if (
            len(batch) < self.batch_size
            and self.drop_last
        ):
            raise StopIteration

        return batch
data = [1, 2, 3, 4, 5, 6, 7]

iterator = BatchIterator(
    data,
    batch_size=3
)

for batch in iterator:
    print(batch)