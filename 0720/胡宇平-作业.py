"""
1.
\d  匹配单个数字  [0-9]  "8"
\w+  1或多个单词字符  [0-9a-zA-Z_]  "word"
^Python 以Python开头的字符串  "Python1"
\d{3,5}  匹配3到5个数字  "1234"
[3-9]  匹配3到9之间的单个数字 "6"
.* 0到任意多个除换行符外的任意字符  "any"
.*?  非贪婪匹配0到任意多个除换行符外的任意字符  "a"

使用原始字符串r""是因为反斜杠不会被转义
"""

"""
2.
None
123
["123","456"]
match检查字符串开头
search在整个字符串中搜索匹配模式的第一个位置
findall返回列表，包括所有匹配结果

match 对象
123
["123","456"]

"""

"""
3.
[1, {"name": "Tom", "scores": [80, 90,95]}]
[1, {"name": "Tom", "scores": [80, 90,95]}]
[1, {"name": "Jerry", "scores": [80, 90]}]
赋值是把对象 的引用传递过去，
浅拷贝创建一个新的外壳，把其中的元素的引用复制过来。这使得shallow[1]和original[1]指向同一个字典
深拷贝递归复制可变对象，所包含的字典是一个新的对象，不是和另外两个共享
"""

""" 
4.
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
inner函数里对count变量做修改，但并没有声明这个变量
第一种方案，nonlocal 
第二种方案 global
"""

""" 
5.
列表是可迭代对象，不是迭代器
字符串是可迭代对象，不是迭代器
字典是可迭代对象，不是迭代器
range(10)是可迭代对象，不是迭代器
iter([1, 2, 3])返回list_iterator，是可迭代对象，是迭代器
enumerate(["a", "b"])是可迭代对象，是迭代器，返回的是enumerate对象
zip([1, 2], ["a", "b"])s是可迭代对象，也是迭代器
123不是可迭代对象，不是迭代器
依据  对应的类型要实现__iter__或__getitem__才是可迭代对象，而迭代器还要实现__next__

for value in [10, 20, 30]:
    print(value)

"""
value = iter([10, 20, 30])
while True:
    try:
        i = next(value)
        print(i)
    except StopIteration:
        break


""" 
6.
"""


class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.step = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.start % 2 != 0:
            self.start += 1
        if self.start >= self.end:
            raise StopIteration
        v = self.start
        self.start += self.step
        return v


""" 
7.
1
2
3
yield返回值，且暂停，保留当前状态，下次从暂停处继续执行
"""

""" 
8.
A before
B before
执行 add
A after
B after
结果: 8

add=deco_b(add)
add=deco_a(add)
从下往上包装即先把函数传给下面的装饰器，
从上往下执行  先从外层的装饰器开始执行其代码
"""
