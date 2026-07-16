student_list = []
menu = """===== 学生信息管理系统（企业进阶版） =====
1. 批量/单个添加学生信息
2. 展示全部学生信息（格式化排版）
3. 多条件查询学生信息
4. 精准修改学生数据（单字段修改）
5. 学生信息删除管理
6. 班级成绩数据统计分析
7. 清空所有学生数据
8. 退出系统"""

while True:
    print(menu)
    opt = input("请选择功能序号：")
    if opt == "1":
        print("----- 添加模式选择 -----")
        print("1. 单个添加学生")
        print("2. 批量连续添加学生")
        medo = input("请选择功能序号")
        if medo == "1":
            id = int(input("请输入学生学号"))
            if id <= 0:
                print("学号必须为正整数，请重新输入！")
                continue
            name = str(input("请输入学生姓名"))
            if len(name) == 0:
                print("姓名不能为空或纯空格，请输入有效姓名！")
                continue
            age = int(input("请输入学生年龄"))
            if age < 1 or age > 30:
                print("年龄必须在1-30范围内，请重新输入！")
                continue
            score = float(input("请输入学生成绩"))
            if score < 0 or score > 100:
                print("0-100范围内，请重新输入！")
                continue
            for stu in student_list:
                if stu["学号"] == id:
                    print(f"{id} 新增失败")
            else:
                student_list.append({"学号": id, "姓名": name, "年龄": age, "成绩": score})
                print(f"学生{id}添加成功")
        elif medo == "2":
            while True:
                id_input = str(input("请输入exit退出"))
                if id_input == 'exit':
                    print("程序退出")
                    break
                id = int(input("请输入学生学号："))
                if id <= 0:
                    print("学号必须为正整数，请重新输入！")
                name = str(input("请输入学生姓名"))
                if len(name) == 0:
                    print("姓名不能为空或纯空格，请输入有效姓名！")
                age = int(input("请输入学生年龄"))
                if age < 1 or age > 30:
                    print("年龄必须在1-30范围内，请重新输入！")
                score = float(input("请输入学生成绩"))

                for stu in student_list:
                    if stu["学号"] == id:
                        print(f"{id} 新增失败")
                        break
                else:
                    student_list.append({"学号": id, "姓名": name, "年龄": age, "成绩": score})
                    print(f"学生{id}添加成功")
                    continue
        else:
            print("输入错误！请输入1-2之间的数字序号")
            break
    # 2. 展示所有学生
    elif opt == "2":
        print("========== 学生信息列表 ==========")
        if len(student_list) == 0:
            print("暂无学生信息，请先添加数据！")
        else:
            print(f"当前在校学生总人数：{len(student_list)}人")
            print("-" * 50)
            if student_list:
                for stu in student_list:
                    print(f"学号：{stu['学号']}\t姓名：{stu['姓名']}\t年龄：{stu['年龄']}成绩：{stu['成绩']}")
            else:
                print("暂无学生考试数据")

    elif opt == "3":
        id = int(input("请输入学生学号："))
        # 遍历stu_list
        for stu in student_list:
            if id == stu["学号"]:
                print(f"学号：{stu['学号']}")
                print(f"姓名：{stu['姓名']}")
                print(f"年龄：{stu['年龄']}")
                print(f"成绩：{stu['成绩']}")
                break
        else:
            print(f"学号：{id} 不存在")

    elif opt == "4":
        id = int(input("请输入学生ID："))
        for stu in student_list:
            if id == stu["学号"]:
                name = str(input("请输入学生姓名："))
                score = float(input("请输入学生成绩："))
                if name:
                    stu["姓名"] = name
                if age:
                    stu["年龄"] = age
                if score:
                    stu["成绩"] = score
                print(f"更新成功！{stu}")
                break
        else:
            print(f"学号：{id} 不存在")

    elif opt == "5":
        id = int(input("请输入学生ID："))
        for stu in student_list:
            if id == stu["学号"]:
                student_list.remove(stu)
                print(f"学号：{id} 删除成功！")
                break
        else:
            print(f"未找到学号：{id} 删除失败！")

    elif opt == "6":
        if len(student_list) == 0:
            print("暂无学生信息，无法进行数据统计！")
            print("=" * 42)
            continue
        score_list = [stu["score"] for stu in student_list]
        total_num = len(student_list)
        total_score = sum(score_list)
        avg_score = total_score / total_num
        max_score = max(score_list)
        min_score = min(score_list)

        pass_count = 0
        fail_count = 0
        for s in score_list:
            if s >= 60:
                pass_count += 1
            else:
                fail_count += 1
        pass_rate = pass_count / total_num * 100
        print(f"学生总人数：{total_num} 人")
        print(f"班级成绩总分：{total_score:.2f}")
        print(f"班级平均分：{avg_score:.2f}")
        print(f"单科最高分：{max_score:.2f}")
        print(f"单科最低分：{min_score:.2f}")
        print(f"及格人数（≥60分）：{pass_count} 人")
        print(f"不及格人数（<60分）：{fail_count} 人")
        print(f"班级及格率：{pass_rate:.2f} %")
    elif opt == "7":
        confirm = input("确认清空全部学生数据？(Y/N)：")
        if confirm == "Y":
            student_list.clear()
            print("所有学生数据已清空！")
    # 8 退出系统
    elif opt == "8":
        tc = input("确认退出学生管理系统？(Y/N)：")
        if tc == "Y":
            print("感谢使用学生信息管理系统，欢迎下次再来！")
            print("程序运行结束")
            break
    else:
        print("输入错误！请输入1-8之间的数字序号")
