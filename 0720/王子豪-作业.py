r"""\d    匹配一个数字
\w+     非单词字符出现1次或多次
^Python     匹配以Python开头的字符
\d{3,5}     匹配连续三到五个数字
[3-9]       匹配3到9中的任意一个数字
.*      匹配任意个任意字符
.*?     尽可能少的匹配任意个字符
r"\d+"是因为r可以防止反斜杠被转义
"""
#==========================
"""None
123
['123','456']
==================
<re.Match object; span=(0, 3), match='123'>
123
['123','456']
"""
#==========================
"""print(original) = [100, {"name": "Tom", "scores": [80,90,95]}]
print(shallow) = [1, {"name": "Tom", "scores": [80,90,95]}]
print(deep) = [1, {"name": "Jerry", "scores": [80,90]}]
print(original[1] is shallow[1]) = True
赋值
shallow[0] = 100
把original列表里的第一个元素更换内存位置，更改到100
shallow[1]["scores"].append(95)
把original列表里的第二个元素的内存位置里的一个scores键的值（列表）加入一个元素95
这里original和shallow共用这个元素的内存位置
deep[1]["name"] = "Jerry"
把deep列表里的第二个元素的内存位置里的一个name键的值改成jerry
"""
#====================
"""错的，因为在最外面有count，这样默认count是全局变量，在子函数里count也被赋值，这是局部变量
会导致错误UnboundLocalError，更改方案：在inner里count += 1前加上nonlocal count，这样修改的是outer里的count
或者在inner里的count前面加上global，这样修改的是全局变量
"""
#=============================
"""可迭代对象：[1, 2, 3]
"hello"
{"name": "Tom"}
range(10)
iter([1, 2, 3]) #这个也是迭代器
enumerate(["a", "b"]) #这个也是迭代器
zip([1, 2], ["a", "b"]) #这个也是迭代器
不可迭代对象：123#因为这个是int，是不可拆分的

lis = [10, 20, 30]
li = iter(lis)
while True:
    try:
        print(next(li))
    except StopIteration:
        break
"""
#=========================
"""EvenNumbers = range(3,13)
a = iter(EvenNumbers)
while True:
    try:
        num = next(a)
        if num%2 == 0:
            print(num)
    except StopIteration:
        print("StopIteration")
        break
"""
#========================
"""1
2
3
return是执行完后返回
yield是执行完这一行就暂停，直接返回，遇到next，再从暂停的地方继续运行
"""




