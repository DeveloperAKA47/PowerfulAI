data = [{"id": 101, "name": "张三", "age": 18, "score": 88.5}]
menu = """===== 学生信息管理系统（企业进阶版） =====
1. 批量/单个添加学生信息
2. 展示全部学生信息（格式化排版）
3. 多条件查询学生信息
4. 精准修改学生数据（单字段修改）
5. 学生信息删除管理
6. 班级成绩数据统计分析
7. 清空所有学生数据
8. 退出系统
请输入功能序号："""


def menuPrint():
    print(menu)


def menuOptionInput():
    i = int(input("input menu option:"))
    return i


def isInt(obj):
    if not obj:
        return False
    return obj.isdigit()


def isFloat(obj):
    if not obj:
        return False
    for i, x in enumerate(obj.split(".")):
        if i > 1:
            return False
        if isInt(x):
            pass
        else:
            return False
    return True


def strCheck(obj):
    obj.strip()
    if not obj:
        return False
    return True


def idCheck(obj):
    if isInt(obj):
        if int(obj) > 0:
            return True
        else:
            return False
    else:
        return False


def nameCheck(obj):
    if strCheck(obj):
        return True
    else:
        return False


def ageCheck(obj):
    if isInt(obj):
        if int(obj) >= 1 and int(obj) <= 30:
            return True
        else:
            return False
    else:
        return False


def isInDataById(id):
    res = [x for x in data if x["id"] == id]
    return res != []


def inputItem():
    input("input id")


def addData():
    opt = input("choose mode,1=单个添加，2=批量添加:")
    if opt == "1":
        pass
    elif opt == "2":
        while True:
            pass


def exitSystem():
    str = input("quit? y/n")
    if str == "y":
        exit()


def main():
    while 1 == 1:
        menuPrint()
        opt = menuOptionInput()
        if opt == 1:
            pass
        if opt == 2:
            pass
        if opt == 3:
            pass
        if opt == 4:
            pass
        if opt == 5:
            pass
        if opt == 6:
            pass
        if opt == 7:
            pass
        if opt == 8:
            exitSystem()


if __name__ == "__name__":
    main()
