from itertools import groupby

import pandas as pd
#从当前目录下的 `sales.csv` 读取数据，并存入 DataFrame `df`。
df = pd.read_csv("sales.csv")
# 显示前 5 行，观察数据结构。
print(df.head())
# 输出 DataFrame 的基本信息
print(df.info())
# 检查各列是否存在缺失值
print(df.isnull().sum())
# 将 **日期** 列转换为 `datetime` 类型。
df["日期"] = pd.to_datetime(df["日期"])
# 添加新列 **销售额
df["销售额"] = df["销量"]*df["单价"]
# 筛选出 **销售额大于 1500** 的所有记录。
print(df.loc[df["销售额"] > 1500])
# 按 **日期** 升序排列整个 DataFrame。
df1 = df.sort_values(by="日期",ascending=True)
print(df1)
# - 按 **产品** 分组，计算：
#   - 总销量
#   - 总销售额
#   - 平均单价
#   - 记录条数（即该产品出现的次数）
df_group = df.groupby("产品").agg({
    "销量":"sum",
    "销售额":"sum",
    "单价":"mean",
    "地区":"count"
})
# - 将结果按总销售额降序排列。
df2 = df_group.sort_values(by="销量",ascending=False)
print(df2)
# 提取 **月份**，按月份分组，统计每月的总销售额和总销量。
df["月份"] = df["日期"].dt.to_period("M")
monthly_summary = df.groupby("月份")[["销售额","销量"]].sum().reset_index()
print(monthly_summary)
# 使用 ExcelWriter 写入多个 Sheet
with pd.ExcelWriter("sales_report.xlsx", engine="xlsxwriter") as writer:
    # Sheet1: 原始清洗后的完整数据（包括新增的“销售额”列）
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    # Sheet2: 按产品分组统计结果（任务4的结果）
    df2.to_excel(writer, sheet_name="Sheet2", index=False)
    # Sheet3: 按月统计结果（任务6的结果）
    monthly_summary.to_excel(writer, sheet_name="Sheet3", index=False)