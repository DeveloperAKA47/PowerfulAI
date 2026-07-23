import re
import collections.abc
from collections.abc import Iterable
import math
import time
from functools import wraps

data1 = [78, "92", " 65.5 ", None, "", True, "abc", 105, 88]


def clean_and_analyze_scores(
    raw_scores: list[object],
) -> dict[str, object]:
    invalid_count = 0
    valid_scores = []
    res = {}
    for i in raw_scores:
        if not i:
            invalid_count += 1
            continue
        if isinstance(i, (int, float)) and not isinstance(i, bool):
            if i < 0 or i > 100 or not math.isfinite(i):
                invalid_count += 1
            else:
                valid_scores.append(i)
        elif isinstance(i, bool):
            invalid_count += 1
        elif isinstance(i, str):
            if not i:
                invalid_count += 1
                continue
            try:
                i = int(i)
                if i < 0 or i > 100 or not math.isfinite(i):
                    invalid_count += 1
                else:
                    valid_scores.append(i)
                continue
            except Exception as e:
                try:
                    i = float(i)
                    if i < 0 or i > 100 or not math.isfinite(i):
                        invalid_count += 1
                    else:
                        valid_scores.append(i)
                    continue
                except Exception as e:
                    invalid_count += 1
                    continue
    if not valid_scores:
        raise ValueError("no valid scores")
    res["valid_scores"] = valid_scores
    res["count"] = len(valid_scores)
    res["total"] = sum(valid_scores)
    res["total"] = round(res["total"], 2)
    res["average"] = sum(valid_scores) / len(valid_scores)
    res["average"] = round(res["average"], 2)
    res["max"] = max(valid_scores)
    res["min"] = min(valid_scores)
    passScore = [x for x in valid_scores if x >= 60]
    res["pass_count"] = len(passScore) if passScore else 0
    excellent = [x for x in valid_scores if x >= 90]
    res["excellent_count"] = len(excellent) if excellent else 0
    res["invalid_count"] = invalid_count
    return res


products2 = [
    {"id": "P001", "name": "键盘", "price": 199.0, "stock": 10},
    {"id": "P002", "name": "鼠标", "price": 89.0, "stock": 25},
    {"id": "P003", "name": "显示器", "price": 1299.0, "stock": 5},
]


def find_product(products: list[dict], product_id: str) -> dict | None:
    for i in products:
        if i["id"] == product_id:
            return i
    return


def update_stock(products: list[dict], product_id: str, change: int) -> int:
    for i in products:
        if i["id"] == product_id:
            i["stock"] += change
            if i["stock"] < 0:
                raise ValueError("stock cannot be negative")
            return i["stock"]
    raise ValueError("product does not exist")


def sell_product(products: list[dict], product_id: str, quantity: int) -> float:
    if isinstance(quantity, int) and not isinstance(quantity, bool) and quantity > 0:
        for i in products:
            if i["id"] == product_id:
                if i["stock"] < quantity:
                    raise ValueError("insufficient stock")
                i["stock"] -= quantity
                return round(i["price"] * quantity, 2)
        raise ValueError("product does not exist")
    else:
        raise ValueError("quantity must be a positive integer")


def inventory_value(products: list[dict]) -> float:
    sum = 0.0
    for i in products:
        sum += i["price"] * i["stock"]
    return round(sum, 2)


"""2026-07-22 15:20:01 | INFO | user=Tom | action=login | duration=125"""
sample_file = "sample.log"
timeRe = re.compile(
    r"^(?P<time>(\d{4})-(0[1-9]|1[0-2])-([0-2][1-9]|10|20|30|31) (\d{2}:\d{2}:\d{2}))"
)
levelRe = re.compile(r"(?P<level>INFO|WARNING|ERROR)")
userRe = re.compile(r"user=(?P<user>\w+)")
actionRe = re.compile(r"action=(?P<action>[a-zA-Z_]+)")
durationRe = re.compile(r"duration=(?P<duration>\d+)")
logRe = re.compile(
    rf"^{timeRe.pattern}\s*\|\s*{levelRe.pattern}\s*\|\s*{userRe.pattern}\s*\|\s{actionRe.pattern}\s*\|\s*{durationRe.pattern}$"
)


def parse_log_line(line: str) -> dict[str, object] | None:
    line = line.strip()
    res = {}
    m = logRe.match(line)
    if not m:
        return
    res["time"] = m.group("time")
    res["level"] = m.group("level")
    res["user"] = m.group("user")
    res["action"] = m.group("action")
    res["duration"] = m.group("duration")
    return res


def iter_log_records(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            res = parse_log_line(line)
            if res:
                yield res


def summarize_logs(file_path: str) -> dict[str, object]:
    valid_count = 0
    level_counts = {}
    duration = []
    slow_users = []
    res = {}
    for i in iter_log_records(file_path):
        valid_count += 1
        level_counts[i["level"]] = level_counts.get(i["level"], 0)
        level_counts[i["level"]] += 1
        duration.append(i["duration"])
        if i["duration"] >= 500:
            slow_users.append(i["user"])
    res["valid_count"] = valid_count
    res["level_counts"] = level_counts
    res["average_duration"] = (
        0.0 if not duration else round(sum(duration) / len(duration), 2)
    )
    res["slow_users"] = sorted(list(set(slow_users)))
    return res


class BatchIterator:
    def __init__(
        self,
        data: Iterable,
        batch_size: int,
        *,
        drop_last: bool = False,
    ):
        self.data = list(data)
        if (
            isinstance(batch_size, int)
            and not isinstance(batch_size, bool)
            and batch_size > 0
        ):
            self.batch_size = batch_size
        else:
            raise ValueError("batch_size must be a positive integer")
        self.drop_last = drop_last
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.data) or (
            self.drop_last and (self.start + self.batch_size) > len(self.data)
        ):
            raise StopIteration
        res = []
        for i in range(self.batch_size):
            if (self.start + i) >= len(self.data):
                break
            res.append(self.data[self.start + i])
        self.start += self.batch_size
        return res


def timer(func):
    @wraps(func)
    def innner(*args, **kwargs):
        start = time.perf_counter()
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            raise Exception
        finally:
            end = time.perf_counter()
            print(f"{func.__name__} took {end-start} seconds")
        return res

    return innner


def retry(
    *,
    max_attempts: int = 3,
    delay: float = 0.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
):
    if (
        isinstance(max_attempts, int)
        and not isinstance(max_attempts, bool)
        and max_attempts > 0
    ):
        if delay >= 0 and math.isfinite(delay):
            pass
        else:
            raise ValueError
    else:
        raise ValueError

    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    res = func(*args, **kwargs)
                    return res
                except exceptions as e:
                    print(e)
                    if i == max_attempts - 1:
                        raise
                    time.sleep(delay)

        return inner

    return outer
