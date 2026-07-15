# 全局数据存储容器
student_list = []
# 主程序循环
while True:
    # ==========================================
    # 1. 渲染主菜单
    # ==========================================
    print("\n===== 学生信息管理系统（企业进阶版） =====")
    print("1. 批量/单个添加学生信息")
    print("2. 展示全部学生信息（格式化排版）")
    print("3. 多条件查询学生信息")
    print("4. 精准修改学生数据（单字段修改）")
    print("5. 学生信息删除管理")
    print("6. 班级成绩数据统计分析")
    print("7. 清空所有学生数据")
    print("8. 退出系统")

    choice = input("请输入功能序号：")

    # ==========================================
    # 2. 功能分支逻辑
    # ==========================================

    # --- 功能 1：添加学生 ---
    if choice == '1':
        print("\n----- 添加模式选择 -----")
        print("1. 单个添加学生")
        print("2. 批量连续添加学生")
        mode = input("请选择录入模式：")

        if mode == '1':
            # 单个添加逻辑
            while True:
                try:
                    # 学号校验
                    id_input = input("请输入学生学号：")
                    if not id_input.isdigit() or int(id_input) <= 0:
                        print(" 学号必须为正整数，请重新输入！")
                        continue
                    new_id = int(id_input)

                    # 查重
                    is_exist = False
                    for s in student_list:
                        if s["id"] == new_id:
                            print(" 该学号已存在，禁止重复录入！当前学生录入终止")
                            is_exist = True
                            break
                    if is_exist: break

                    # 姓名校验
                    name = input("请输入学生姓名：").strip()
                    if not name:
                        print(" 姓名不能为空或纯空格，请输入有效姓名！")
                        continue

                    # 年龄校验
                    age_input = input("请输入学生年龄：")
                    if not age_input.isdigit():
                        print(" 年龄必须为数字，请重新输入！")
                        continue
                    age = int(age_input)
                    if age < 1 or age > 30:
                        print(" 年龄必须在1-30范围内，请重新输入！")
                        continue

                    # 分数校验
                    score_input = input("请输入学生分数：")
                    score = float(score_input)
                    if score < 0 or score > 100:
                        print(" 分数必须在0-100范围内，请重新输入！")
                        continue

                    # 添加到列表
                    student_list.append({"id": new_id, "name": name, "age": age, "score": score})
                    print(" 学生信息添加成功！")
                    print(f"【新增学生信息】 学号：{new_id} 姓名：{name} 年龄：{age} 分数：{score}")
                    break  # 跳出输入循环

                except ValueError:
                    print(" 输入格式错误，分数请输入数字！")

        elif mode == '2':
            # 批量添加逻辑
            print("\n===== 批量录入模式 =====")
            print("提示：输入exit可退出批量录入")
            while True:
                id_input = input("请输入学生学号：")
                if id_input.lower() == 'exit':
                    print("退出批量录入模式，返回主菜单")
                    break

                try:
                    if not id_input.isdigit() or int(id_input) <= 0:
                        print(" 学号必须为正整数，请重新输入！")
                        continue
                    new_id = int(id_input)

                    # 查重
                    is_exist = False
                    for s in student_list:
                        if s["id"] == new_id:
                            print(" 该学号已存在，禁止重复录入！当前学生录入终止")
                            is_exist = True
                            break
                    if is_exist: continue

                    name = input("请输入学生姓名：").strip()
                    if not name:
                        print(" 姓名不能为空或纯空格，请输入有效姓名！")
                        continue

                    age = int(input("请输入学生年龄："))
                    if age < 1 or age > 30:
                        print(" 年龄必须在1-30范围内，请重新输入！")
                        continue

                    score = float(input("请输入学生分数："))
                    if score < 0 or score > 100:
                        print(" 分数必须在0-100范围内，请重新输入！")
                        continue

                    student_list.append({"id": new_id, "name": name, "age": age, "score": score})
                    print("学生信息添加成功！")

                except ValueError:
                    print(" 输入格式错误，请检查数字！")
        else:
            print(" 无效的菜单选项！")

    # --- 功能 2：展示全部 ---
    elif choice == '2':
        print("\n========== 学生信息列表 ==========")
        if len(student_list) == 0:
            print("暂无学生信息，请先添加数据！")
        else:
            print(f"当前在校学生总人数：{len(student_list)}人")
            print("--------------------------------")
            for s in student_list:
                print(f"学号：{s['id']} 姓名：{s['name']} 年龄：{s['age']} 分数：{s['score']}")
            print("================================")

    # --- 功能 3：查询 ---
    elif choice == '3':
        print("\n----- 查询功能子菜单 -----")
        print("1. 学号精准查询")
        print("2. 姓名模糊查询")
        print("3. 分数区间查询")
        sub_choice = input("请选择查询方式：")

        if sub_choice == '1':
            try:
                q_id = int(input("请输入查询学号："))
                found = False
                for s in student_list:
                    if s['id'] == q_id:
                        print(f" 查询成功！ 学号：{s['id']} 姓名：{s['name']} 年龄：{s['age']} 分数：{s['score']}")
                        found = True
                        break
                if not found:
                    print(" 未找到对应学号的学生！")
            except ValueError:
                print(" 学号必须是数字！")

        elif sub_choice == '2':
            keyword = input("请输入姓名关键字：")
            has_result = False
            print("========== 模糊查询结果 ==========")
            for s in student_list:
                if keyword in s['name']:
                    print(f"学号：{s['id']} 姓名：{s['name']} 年龄：{s['age']} 分数：{s['score']}")
                    has_result = True
            if not has_result:
                print(" 未找到包含该关键字的学生！")

        elif sub_choice == '3':
            try:
                min_s = float(input("请输入最低分数："))
                max_s = float(input("请输入最高分数："))
                if min_s > max_s:
                    print(" 最低分不能大于最高分！")
                else:
                    has_result = False
                    print("========== 区间查询结果 ==========")
                    for s in student_list:
                        if min_s <= s['score'] <= max_s:
                            print(f"学号：{s['id']} 姓名：{s['name']} 年龄：{s['age']} 分数：{s['score']}")
                            has_result = True
                    if not has_result:
                        print(" 该分数段内无学生数据！")
            except ValueError:
                print(" 分数必须是数字！")
        else:
            print(" 无效的菜单选项！")

    # --- 功能 4：修改 ---
    elif choice == '4':
        try:
            m_id = int(input("请输入需要修改的学生学号："))
            target = None
            for s in student_list:
                if s['id'] == m_id:
                    target = s
                    break

            if target is None:
                print(" 该学号不存在，无法修改！")
            else:
                print("\n----- 修改功能子菜单 -----")
                print("1. 修改姓名")
                print("2. 修改年龄")
                print("3. 修改分数")
                print("4. 返回上一级")
                op = input("请选择修改字段：")

                if op == '1':
                    new_name = input("请输入新的姓名：").strip()
                    if new_name:
                        target['name'] = new_name
                        print(" 学生信息修改成功！")
                    else:
                        print(" 姓名不能为空！")
                elif op == '2':
                    new_age = int(input("请输入新的年龄："))
                    if 1 <= new_age <= 30:
                        target['age'] = new_age
                        print(" 学生信息修改成功！")
                    else:
                        print(" 年龄必须在1-30范围内！")
                elif op == '3':
                    new_score = float(input("请输入新的分数："))
                    if 0 <= new_score <= 100:
                        target['score'] = new_score
                        print(" 学生信息修改成功！")
                    else:
                        print(" 分数必须在0-100范围内！")
                elif op == '4':
                    pass  # 返回
                else:
                    print(" 无效选项！")

                # 显示结果
                if target and op in ['1', '2', '3']:
                    print(
                        f"【最新学生信息】 学号：{target['id']} 姓名：{target['name']} 年龄：{target['age']} 分数：{target['score']}")
        except ValueError:
            print(" 输入格式错误！")

    # --- 功能 5：删除 ---
    elif choice == '5':
        print("\n----- 删除功能子菜单 -----")
        print("1. 学号单条删除")
        print("2. 清空全部学生数据")
        del_choice = input("请选择删除模式：")

        if del_choice == '1':
            try:
                d_id = int(input("请输入待删除学生学号："))
                found_idx = -1
                for i in range(len(student_list)):
                    if student_list[i]['id'] == d_id:
                        found_idx = i
                        break

                if found_idx != -1:
                    student_list.pop(found_idx)
                    print(f" 学号{d_id}学生信息删除成功！")
                else:
                    print(" 删除失败，未找到该学号！")
            except ValueError:
                print(" 学号必须是数字！")

        elif del_choice == '2':
            confirm = input("确认清空所有学生数据？该操作不可逆！(Y/N)：")
            if confirm.upper() == 'Y':
                student_list.clear()
                print(" 已清空全部学生信息！")
        else:
            print(" 无效选项！")

    # --- 功能 6：统计 ---
    elif choice == '6':
        print("\n========== 班级成绩统计报表 ==========")
        if len(student_list) == 0:
            print("暂无学生数据，无法进行统计分析！")
        else:
            count = len(student_list)
            total_score = 0
            max_score = student_list[0]['score']
            min_score = student_list[0]['score']
            pass_count = 0

            for s in student_list:
                sc = s['score']
                total_score += sc
                if sc > max_score: max_score = sc
                if sc < min_score: min_score = sc
                if sc >= 60: pass_count += 1

            avg_score = total_score / count
            fail_count = count - pass_count
            pass_rate = (pass_count / count) * 100

            print(f"学生总人数：{count} 人")
            print(f"成绩总分：{total_score:.2f}")
            print(f"平均分：{avg_score:.2f} 分")
            print(f"最高分：{max_score:.2f} 分")
            print(f"最低分：{min_score:.2f} 分")
            print("--------------------------------")
            print(f"及格人数：{pass_count} 人")
            print(f"不及格人数：{fail_count} 人")
            print(f"班级及格率：{pass_rate:.2f} %")
            print("================================")

    # --- 功能 7：清空 (独立入口) ---
    elif choice == '7':
        confirm = input("⚠️ 确认清空所有学生数据？该操作不可逆！(Y/N)：")
        if confirm.upper() == 'Y':
            student_list.clear()
            print(" 已清空全部学生信息！")

    # --- 功能 8：退出 ---
    elif choice == '8':
        confirm = input("⚠️ 确认退出学生管理系统？(Y/N)：")
        if confirm.upper() == 'Y':
            print("感谢使用学生信息管理系统，欢迎下次再来！")
            print("程序运行结束")
            break

    # --- 异常输入处理 ---
    else:
        print(" 输入序号超出范围！请输入1-8之间的数字")