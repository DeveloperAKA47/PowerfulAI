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


def clearAll(table):
    if table == []:
        return
    table.clear()


def twiceCheck():
    s = input("are you sure.Y/N:").strip()
    if s == "Y":
        return 0
    return -1


def itemPrint(obj):
    print(
        f"学号：{obj['id']}  姓名：{obj['name']}  年龄：{obj['age']}  分数：{obj['score']:.2f}"
    )
    return


def tablePrint(dictionsInList):
    if data == []:
        return -1
    print("========== 学生信息列表 ==========")
    print(f"当前在校学生总人数：{len(data)}人")
    for x in dictionsInList:
        itemPrint(x)


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


def scoreCheck(obj):
    if isInt(obj) or isFloat(obj):
        if float(obj) >= 0 and float(obj) <= 100:
            return True
        else:
            return False
    else:
        return False


def isInDataById(id):
    res = [x for x in data if x["id"] == id]
    return res != []


def inputItem():
    while True:
        id = input("input id:")
        if id == "exit":
            return -1
        if idCheck(id):
            break
        print("输入不合法，请重新输入。")
    id = int(id)
    while True:
        name = input("input name:")
        if name == "exit":
            return -1
        if nameCheck(name):
            break
        print("输入不合法，请重新输入。")
    while True:
        age = input("input age:")
        if age == "exit":
            return -1
        if ageCheck(age):
            break
        print("输入不合法，请重新输入。")
    age = int(age)
    while True:
        score = input("input score:")
        if score == "exit":
            return -1
        if scoreCheck(score):
            break
        print("输入不合法，请重新输入。")
    score = int(score) if isInt(score) else float(score)
    data.append({"id": id, "name": name, "age": age, "score": score})
    print(f"✅ 学生信息添加成功！")
    return 0


def addData():
    opt = input("choose mode,1=单个添加，2=批量添加:")
    if opt == "1":
        inputItem()
    elif opt == "2":
        while True:
            if inputItem() < 0:
                break


def getInfoById(id):
    if isInDataById(id):
        tablePrint([x for x in data if x["id"] == id])
    else:
        print("no info match")
        return


def getInfoByName(s):
    res = list(filter(lambda x: s in x["name"], data))
    if res == []:
        print("no info match")
        return
    else:
        tablePrint(res)


def getInfoByScore(low, high):
    res = list(filter(lambda x: (low <= x["score"] and high >= x["score"]), data))
    if res == []:
        print("no info match")
        return
    else:
        tablePrint(res)


def selectInfo():
    while True:
        print("1.学号精准查询 2.姓名模糊查询 3.分数区间查询 0.结束查询")
        opt = int(input("请选择查询方式："))
        if opt == 1:
            id = int(input("请输入查询学号："))
            getInfoById(id)
        if opt == 2:
            s = input("请输入姓名关键字：")
            getInfoByName(s)
        if opt == 3:
            low = float(input("请输入最低分数："))
            high = float(input("请输入最高分数："))
            getInfoByScore(low, high)
        if opt == 0:
            return


def updateInfo():
    id = int(input("输入学号:"))
    if isInDataById(id):
        while True:
            print("""----- 修改功能子菜单 -----
1. 修改姓名
2. 修改年龄
3. 修改分数
4. 返回上一级""")
            opt = int(input("请选择修改字段："))
            if opt == 4:
                break
            elif opt == 1:
                name = input("input name:")
                if nameCheck(name):
                    res = [x for x in data if x["id"] == id]
                    res[0]["name"] = name
                    res = [x for x in data if x["id"] == id]
                    print("✅ 学生信息修改成功！")
                    tablePrint(res)
                else:
                    print("invalid inputs")
                    continue
            elif opt == 2:
                age = input("input age:")
                if ageCheck(age):
                    res = [x for x in data if x["id"] == id]
                    age = int(age)
                    res[0]["age"] = age
                    res = [x for x in data if x["id"] == id]
                    print("✅ 学生信息修改成功！")
                    tablePrint(res)
                else:
                    print("invalid inputs")
                    continue
            elif opt == 3:
                score = input("input score:")
                if scoreCheck(score):
                    res = [x for x in data if x["id"] == id]
                    score = int(score) if isInt(score) else float(score)
                    res[0]["score"] = score
                    res = [x for x in data if x["id"] == id]
                    print("✅ 学生信息修改成功！")
                    tablePrint(res)
                else:
                    print("invalid inputs")
                    continue

    else:
        print("no info match")


def deleteInfo():
    print("""----- 删除功能子菜单 -----
1. 学号单条删除
2. 清空全部学生数据""")
    opt = input("请选择删除模式：").strip()
    if opt == "1":
        id = input("input id:")
        if idCheck(id):
            id = int(id)
            if isInDataById(id):
                res = {k: v for k, v in enumerate(data) if id == v["id"]}
                for i in res.keys():
                    data.pop(i)
                    break
                print("delete success")
            else:
                print("no match info.fail")
        else:
            return
    if opt == "2":
        if twiceCheck() == 0:
            clearAll(data)


def statisticsOfData():
    if data == []:
        print("暂无数据")
        return
    print(f"学生总人数 {len(data)}", end="\t")
    print(f"成绩总分 {sum([x['score'] for x in data])}", end="\t")
    print(f"平均分 {sum([x['score'] for x in data])/len(data):.2f}", end="\t")
    print(f"最高分 {max([x['score'] for x in data])}", end="\t")
    print(f"最低分 {min([x['score'] for x in data])}", end="\t")
    res1 = [x["score"] for x in data if x["score"] >= 60]
    if res1 == []:
        passedCount = 0
    else:
        passedCount = len(res1)
    res2 = [x["score"] for x in data if x["score"] < 60]
    if res2 == []:
        failCount = 0
    else:
        failCount = len(res2)
    print(f"及格人数 {passedCount}")
    print(f"不及格人数 {failCount}")
    print(f"及格率 {passedCount/(passedCount+failCount):.2f}")


def exitSystem():
    str = input("quit? y/n").strip()
    if str == "y":
        exit()


def main():
    while 1 == 1:
        menuPrint()
        opt = menuOptionInput()
        if opt == 1:
            addData()
        if opt == 2:
            if tablePrint(data) == -1:
                print("暂无学生信息，请先添加数据")
        if opt == 3:
            selectInfo()
        if opt == 4:
            updateInfo()
        if opt == 5:
            deleteInfo()
        if opt == 6:
            statisticsOfData()
        if opt == 7:
            if twiceCheck() == 0:
                clearAll(data)
                print("clear success")
        if opt == 8:
            exitSystem()


if __name__ == "__main__":
    main()
