from asyncio import staggered
from idlelib.configdialog import changes


def main():
    student_base = []
    MENU = """===== 学生信息管理系统（企业进阶版） =====
1. 批量/单个添加学生信息
2. 展示全部学生信息（格式化排版）
3. 多条件查询学生信息
4. 精准修改学生数据（单字段修改）
5. 学生信息删除管理
6. 班级成绩数据统计分析
7. 清空所有学生数据
8. 退出系统
请输入功能序号："""
    def menu():
        print(MENU)

    def check():
        while True:
            option = input()
            if option == "":
                print("输入为空，请重新输入")
                continue
            try:
                opt = int(option)
                return opt
            except  ValueError:
                print("输入无效！请输入整数。")

    def function1():
        minimenu = """----- 添加模式选择 -----
1. 单个添加学生
2. 批量连续添加学生
        """
        print(minimenu)
        print("请选择录入模式：")
        choice = check()
        if choice == 1:
            print("请输入学生学号：")
            sid = check()
            if sid <= 0:
                print("学号必须为正整数，请重新输入！")
                return None
            for i in student_base:
                if i["sid"] == sid:
                    print("该生信息已录入")
                    return None
            sname = input("请输入学生姓名：")
            if sname == "":
                print("姓名不能为空或纯空格，请输入有效姓名！")
                return None
            if len(sname) > 10:
                print("姓名不能超过10个字")
                return None
            print ("请输入学生年龄")
            sage = check()
            if sage <= 1 or sage >= 30:
                print("年龄必须在1-30范围内，请重新输入！")
                return None
            while True:
                score = input("请输入学生成绩")
                if score == "":
                    print("成绩不能为空")
                    continue
                try:
                    score = float(score)
                    if score < 0  or  score > 100:
                        print("分数必须在0-100范围内，请重新输入！")
                    else:
                        break
                except ValueError:
                    print("成绩请输入数字")
            student_base.append({"学号": sid,"姓名": sname,"年龄": sage,"分数": score})
            print("✅ 学生信息添加成功！")
            print("【新增学生信息】")
            print(f"学号: {sid},姓名: {sname},年龄: {sage},分数: {score}")
        elif choice == 2:
            pass
        else:
            print("输入无效！请输入有效的功能编号。")


    while True:
        menu()
        opt = check()
        if opt == 1:
            function1()
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            pass
        elif opt == 5:
            pass
        elif opt == 6:
            pass
        elif opt == 7:
             pass
        elif opt == 8:
            pass
            break
        else:
            pass














main()