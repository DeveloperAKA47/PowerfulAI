student_list = [{"学号":101,"姓名":"tom","年龄":18,"分数":60.0},
                 {"学号":102,"姓名":"ji","年龄":26,"分数":88.0},
                 {"学号":103,"姓名":"jklove","年龄":22,"分数":100.0},
                 {"学号":104,"姓名":"mt","年龄":24,"分数":98.0}
                ]
asd = """===== 学生信息管理系统（企业进阶版） =====
1. 批量/单个添加学生信息
2. 展示全部学生信息（格式化排版）
3. 多条件查询学生信息
4. 精准修改学生数据（单字段修改）
5. 学生信息删除管理
6. 班级成绩数据统计分析
7. 清空所有学生数据
8. 退出系统"""
"""字段名	数据类型	约束规则	唯一性
id(学号)	整型 int	必须为正整数,禁止0、负数、字符、空值	全局唯一，不可重复
name(姓名)	字符串 str	非空、非纯空格，必须输入有效中/英文字符	不唯一
age(年龄)	整型 int	取值范围 1-30,超限无效，禁止非数字输入	不唯一
score(分数)	浮点型/整型	取值范围 0-100,支持整数、小数，超限无效	不唯一"""


def a1():
    # 本功能支持单条录入、批量连续录入两种模式，全覆盖数据合法性校验与重复校验，杜绝非法、重复数据入库。
    # 模式选择：进入功能后优先选择模式，1 = 单个添加，2 = 批量添加
    # 重复校验：录入学号后，全局遍历校验学号唯一性，重复则立即提示并终止当前录入
    # 全字段校验：严格遵循3.2字段约束规则，任意字段非法则重新输入，无跳过机制
    # 批量录入交互：支持连续录入，用户可输入指定退出指令终止批量模式
    # 结果反馈：录入成功后提示成功信息，并展示当前新增学生完整数据
    print("1.单个添加学生信息")
    print("2.批量添加学生信息")
    opt1 = int(input("请输入你的选择:"))
    if opt1 == 1:
        print("添加学生信息模式")
        id = int(input("请输入学号:"))
        for stu in student_list:
            if stu["学号"] == id:
                print("学号已存在，新增失败")
                break
            if id <= 0:
                print("学号必须为正整数，新增失败")
                break
        else:
            name = input("请输入姓名:")
            if len(name.strip()) == 0:
                print("姓名不能为空，新增失败")
                return
            age = int(input("请输入年龄:"))
            if age < 1 or age > 30:
                print("年龄必须在1-30之间，新增失败")
                return
            score = float(input("请输入分数:"))
            if score < 0 or score > 100:
                print("分数必须在0-100之间，新增失败")
                return
            student_list.append({"学号": id, "姓名": name, "年龄": age, "分数": score})
            print("输入成功")
    elif opt1 == 2:
        while True:
            print("批量添加学生信息模式")
            opt2 = int(input("输入1退出,输入其他任意键继续添加:"))
            if opt2 == 1:
                break
            id = int(input("请输入学号:"))
            for stu in student_list:
                if stu["学号"] == id:
                    print("学号已存在，新增失败")
                    break
                if id <= 0:
                    print("学号必须为正整数，新增失败")
                    break
            else:
                name = input("请输入姓名:")
                if len(name.strip()) == 0:
                    print("姓名不能为空，新增失败")
                    break
                age = int(input("请输入年龄:"))
                if age < 1 or age > 30:
                    print("年龄必须在1-30之间，新增失败")
                    break
                score = float(input("请输入分数:"))
                if score < 0 or score > 100:
                    print("分数必须在0-100之间，新增失败")
                    break
                student_list.append({"学号": id, "姓名": name, "年龄": age, "分数": score})
                print("新增成功")
                print(f"学号:{id},姓名:{name},年龄:{age},分数:{score}")
    else:
        print("输入错误")


def a2():
    # 标准化格式化输出，禁止原始字典直接打印，保证控制台界面整洁规整，具备空数据容错能力。
    # 空数据处理：学生列表为空时，输出友好提示：暂无学生信息，请先添加数据
    # 格式化展示：采用对齐排版，清晰展示学号、姓名、年龄、分数四大字段
    # 数据统计：自动展示当前系统内学生总人数
    if len(student_list) == 0:
        print("暂无学生信息，请先添加数据")
    else:
        print("学号\t姓名\t年龄\t分数")
        for stu in student_list:
            print(f"{stu['学号']}\t{stu['姓名']}\t{stu['年龄']}\t{stu['分数']}")
        print(f"当前系统内学生总人数为:{len(student_list)}")


def a3():
    # 学号精准查询：输入学号全局遍历匹配，精准定位单条数据，无匹配则提示无对应学生
    # 姓名模糊查询：支持关键字匹配，筛选所有包含指定关键字的学生，支持同名多数据查询
    # 分数区间查询：输入最低分、最高分，筛选区间内所有学生，区间输入非法则提示重新输入
    # 容错机制：所有查询场景无匹配数据时，友好提示，程序无报错、无崩溃
    print("请选择查询方式:1学号精准查询,2姓名模糊查询,3分数区间查询")
    opt3 = int(input("请输入你的选择:"))
    if opt3 == 1:
        id = int(input("请输入学号:"))
        for stu in student_list:
            if stu["学号"] == id:
                print(f"学号:{stu['学号']},姓名:{stu['姓名']},年龄:{stu['年龄']},分数:{stu['分数']}")
                break
        else:
            print("无对应学生")
    elif opt3 == 2:
        name = input("请输入姓名关键字:")
        for stu in student_list:
            if name in stu["姓名"]:
                print(f"学号:{stu['学号']},姓名:{stu['姓名']},年龄:{stu['年龄']},分数:{stu['分数']}")
        else:
            print("无对应学生")
    elif opt3 == 3:
        min_score = float(input("请输入最低分:"))
        max_score = float(input("请输入最高分:"))
        for stu in student_list:
            if min_score <= float(stu["分数"]) <= max_score:
                print(f"学号:{stu['学号']},姓名:{stu['姓名']},年龄:{stu['年龄']},分数:{stu['分数']}")
        else:
            print("无对应学生")


def a4():
    # 支持单字段独立修改，无需全覆盖重写数据，修改数据二次校验，保障数据合规性。
    # 前置校验：输入待修改学号，遍历校验学号是否存在，不存在直接终止修改流程
    # 修改子菜单：1.修改姓名2.修改年龄3.修改分数4.返回上一级
    # 字段隔离修改：仅更新用户指定字段，保留其他原有数据，避免无效操作
    # 后置校验：修改内容必须遵循全局字段约束，非法数据禁止保存
    # 结果反馈：修改成功后展示学生最新完整信息
    id = int(input("请输入待修改学生学号:"))
    for stu in student_list:
        if stu["学号"] == id:
            print("请输入你的选择:1.修改姓名2.修改年龄3.修改分数4.返回上一级")
            opt4 = int(input("请输入你的选择:"))
            if opt4 == 1:
                name = input("请输入新的姓名：")
                stu["姓名"] = name
                print(f"修改成功,学号:{stu['学号']},姓名:{stu['姓名']},年龄:{stu['年龄']},分数:{stu['分数']}")
            elif opt4 == 2:
                age = int(input("请输入新的年龄："))
                stu["年龄"] = age
                print(f"修改成功,学号:{stu['学号']},姓名:{stu['姓名']},年龄:{stu['年龄']},分数:{stu['分数']}")
            elif opt4 == 3:
                score = float(input("请输入新的分数："))
                stu["分数"] = score
                print(f"修改成功,学号:{stu['学号']},姓名:{stu['姓名']},年龄:{stu['年龄']},分数:{stu['分数']}")
            elif opt4 == 4:
                break
            else:
                print("输入错误，请重新输入")


def a5():
    # 支持单条删除、批量清空双模式，配备二次防误删确认机制，全场景边界容错。
    # 删除子菜单：1.学号单条删除2.清空全部学生数据
    # 单条删除：精准匹配学号，存在则删除并提示成功，不存在则提示删除失败
    # 清空删除：强制二次确认，输入Y确认清空、N取消操作，防止误操作数据丢失
    # 空数据容错：列表为空时执行删除操作，友好提示，程序正常运行无异常
    print("请输入你的选择:1.学号单条删除2.清空全部学生数据")
    opt5 = int(input("请输入你的选择："))
    if opt5 == 1:
        id = int(input("请输入待删除学生学号:"))
        for stu in student_list:
            if stu["学号"] == id:
                student_list.remove(stu)
                print("删除成功")
                break
        else:
            print("无对应学生,删除失败")
    elif opt5 == 2:
        confirm = input("确认清空全部学生数据？输入Y确认，N取消：")
        if confirm == "Y":
            student_list.clear()
            print("已清空全部学生数据")
        elif confirm == "N":
            print("已取消操作")
        else:
            print("输入错误，请重新输入")


def a6():
    # 班级成绩数据统计分析
    # 基于基础遍历完成数据统计，无任何算法，输出标准化统计报表，保留固定小数位数。
    # 空数据保护：无学生数据时提示暂无统计数据，禁止程序报错
    # 基础统计项：学生总人数、成绩总分、平均分（保留2位小数）、最高分、最低分
    # 分层统计项：及格人数（≥60）、不及格人数、及格率（保留2位小数）
    if len(student_list) == 0:
        print("暂无统计数据")
    else:
        total_students = len(student_list)
        total_score = sum(stu["分数"] for stu in student_list)
        average_score = total_score / total_students
        max_score = max(stu["分数"] for stu in student_list)
        min_score = min(stu["分数"] for stu in student_list)
        yx_count = len([stu for stu in student_list if stu["分数"] >= 90])
        lh_count = len([stu for stu in student_list if 90>stu["分数"] >= 70])
        jg_count = len([stu for stu in student_list if stu["分数"] >= 60 and stu["分数"] < 70])
        bjg_count = total_students - yx_count - lh_count - jg_count
        pass_rate = (total_students - bjg_count) / total_students * 100
        print(f"学生总人数:{total_students},成绩总分:{total_score},平均分:{average_score:.2f},最高分:{max_score},最低分:{min_score}")
        print(f"优秀人数：{yx_count},良好人数{lh_count},及格人数:{jg_count},不及格人数:{bjg_count},及格率:{pass_rate:.2f}%")


def a7():
    # 清空所有学生数据：强制二次确认，输入Y确认清空、N取消操作，防止误操作数据丢失
    confirm = input("确认清空全部学生数据？输入Y确认，N取消：")
    if confirm == "Y":
        student_list.clear()
        print("已清空全部学生数据")
    elif confirm == "N":
        print("已取消操作")
    else:
        print("输入错误，请重新输入")


while True:
    print(asd)
    opt = int(input("请输入功能序号："))
    if opt == 1:
        a1()
    elif opt == 2:
        a2()
    elif opt == 3:
        a3()
    elif opt == 4:
        a4()
    elif opt == 5:
        a5()
    elif opt == 6:
        a6()
    elif opt == 7:
        a7()
    elif opt == 8:
        # 防误退二次确认机制，用户确认后终止主循环、退出程序，取消则返回主菜单，保障操作安全性。
        confirm = input("确认退出程序？输入Y确认，N取消：")
        if confirm == "Y":
            print("感谢使用，再见！")
            break
        elif confirm == "N":
            print("已取消操作")
        else:
            print("输入错误，请重新输入")
    else:
        print("输入错误，请输入1-8之间的数字")
