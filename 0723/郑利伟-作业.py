# 第 1 题：成绩清洗与统计
import math
from random import sample

# 示例数据：包含整数、浮点数、字符串、空值、布尔值、非法字符串、越界分数以及 nan/inf 等情况
# 这里用来测试函数对多种输入类型的清洗和统计能力
data = [78, "92", " 65.5 ", None, "", True, "abc", 105, 88]


def clean_and_analyze_scores(raw_scores: list[object]) -> dict[str, object]:
    """清洗成绩数据并进行统计，返回包含有效成绩和统计结果的字典。"""
    # 存放最终确认合法的成绩列表
    valid_scores = []
    # 记录所有被判定为非法的数据个数
    invalid_count = 0

    for item in raw_scores:
        # 布尔值必须视为非法数据，不能将 True/False 当成 1/0
        if isinstance(item, bool):
            invalid_count += 1
            continue

        # 处理整数、浮点数和字符串类型的数据
        # 整数和浮点数可以直接参与计算；字符串则先去除空白，再尝试转换为数字
        if isinstance(item, (int, float)):
            score = float(item)
        elif isinstance(item, str):
            text = item.strip()
            # 空字符串或仅包含空白的字符串视为非法数据
            if not text:
                invalid_count += 1
                continue
            try:
                score = float(text)
            except ValueError:
                # 例如 "abc" 这类无法转换为数字的字符串，视为非法数据
                invalid_count += 1
                continue
        else:
            # None 以及其他未知类型都算作非法数据
            invalid_count += 1
            continue

        # 合法分数必须是有限值，并且落在 0 到 100 之间
        # math.isfinite() 可以避免 nan、inf 这类非法数值进入合法成绩列表
        if not math.isfinite(score):
            invalid_count += 1
            continue

        if not 0 <= score <= 100:
            invalid_count += 1
            continue

        # 通过上述检查的数字才算是合法成绩，加入列表中
        valid_scores.append(score)

    # 如果没有任何合法成绩，就抛出异常，提示调用者没有可统计的数据
    if not valid_scores:
        raise ValueError("no valid scores")

    # 对总分和平均分保留两位小数
    total = round(sum(valid_scores), 2)
    average = round(total / len(valid_scores), 2)

    return {
        "valid_scores": valid_scores,
        "count": len(valid_scores),
        "total": total,
        "average": average,
        "max": max(valid_scores),
        "min": min(valid_scores),
        "pass_count": sum(1 for score in valid_scores if score >= 60),
        "excellent_count": sum(1 for score in valid_scores if score >= 90),
        "invalid_count": invalid_count,
    }


if __name__ == "__main__":
    # 在脚本运行时调用函数并打印结果，方便直接查看输出
    print(clean_and_analyze_scores(data))


# 第 2 题：商品库存管理
products = [
    {"id": "P001", "name": "键盘", "price": 199.0, "stock": 10},
    {"id": "P002", "name": "鼠标", "price": 89.0, "stock": 25},
    {"id": "P003", "name": "显示器", "price": 1299.0, "stock": 5},
]
def find_product(products: list[dict], product_id: str) -> dict | None:
    #根据商品编号查找商品，找到则返回商品字典，否则返回 None
    for product in products:
        if product["id"] == product_id:
            return product
    return None
def update_stock(products: list[dict], product_id: str, change: int) -> int:
    # 增加或减少某个商品的库存，成功后返回新的库存数量
    product = find_product(products, product_id)
    #如果商品不存在则抛出异常
    if product is None:
        raise ValueError("product does not exist")
    new_stock = product["stock"] + change
    #如果修改后库存小于0则抛出异常
    if new_stock < 0:
        raise ValueError("stock cannot be negative")
    product["stock"] = new_stock
    return new_stock
def sell_product(products: list[dict], product_id: str, quantity: int) -> float:
    # 销售商品，返回销售总价
    product = find_product(products, product_id)
    #商品不存在抛出异常
    if product is None:
        raise ValueError("product does not exist")
    #库存不足抛出异常
    if product["stock"] < quantity:
        raise ValueError("insufficient stock")
    product["stock"] = product["stock"] - quantity
    return product["stock"]
def inventory_value(products: list[dict]) -> float:
    # 计算所有商品库存的总价值
    total_value = 0.0
    for product in products:
        total_value += product["price"] * product["stock"]
        return total_value

print(find_product(products, "P001"))
print(find_product(products, "P005"))
try:
    print(update_stock(products, "P001", -20))
except Exception as e:
    print("操作失败",e)
print(update_stock(products, "P002", 2))
print(sell_product(products, "P001", 2))
print(f"{inventory_value(products)}")


# 第 3 题：日志解析与汇总
import re
sample = "2026-07-22 15:20:01 | INFO | user=Tom | action=login | duration=125"
def parse_log_line(line: str) -> dict[str, object] | None:

    # 字段用` | ` 分隔，两侧允许多余空格。
    parts = [part.strip() for part in line.split("|")]
    if len(parts) != 5:
        return None
    time, level, user, action, duration = parts
    # 检查时间格式
    match = re.search(r"(?P<time>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})-"
                      r"(?P<level>\w+(INFO|WARNING|ERROR))-"
                      r"(?P<user>\w)-(?P<action>\[a-z][A-Z]|_)-"
                      r"(?P<duration>\d{4})",sample)
    print(time, level, user, action, duration)
    if match is None:
        return None
parse_log_line(sample)
def iter_log_records(file_path: str):
    pass


def summarize_logs(file_path: str) -> dict[str, object]:
    pass


#第 4 题：批处理迭代器


#第 5 题：重试与计时装饰器

# 第6题