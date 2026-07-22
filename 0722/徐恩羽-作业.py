import pandas as pd
import copy
# 从当前目录下的 sales.csv 读取数据，并存入 DataFrame df。
DataFrame=pd.read_csv('sales.csv')
# 显示前 5 行，观察数据结构。
print(DataFrame.head(5))
# 输出 DataFrame 的基本信息（列名、非空数量、数据类型）。
print(DataFrame.describe())
# 检查各列是否存在缺失值，若有则处理（自行决定填充或删除，并说明理由）。
print(DataFrame.notna())
# 添加新列 销售额，计算公式为：销量 * 单价。
DataFrame['销售额']=DataFrame['销量']*DataFrame['单价']
a=copy.deepcopy(DataFrame)
# 将 日期 列转换为 datetime 类型。
DataFrame['日期']=pd.to_datetime(DataFrame['日期'])
# 将 产品 列转换为 category 类型，节省内存（可选）。
# 3. 数据筛选与排序
# 筛选出 销售额大于 1500 的所有记录。
print(DataFrame.loc[DataFrame['销售额']>1500])
# 按 日期 升序排列整个 DataFrame。
print(DataFrame.sort_values('日期'))
# 4. 分组统计（基础）
# 按 产品 分组，计算：
# 总销量
# 总销售额
# # 平均单价
# 记录条数（即该产品出现的次数）
group=DataFrame.groupby('产品',as_index=False).agg({
    '销量': 'sum',
    '销售额': 'sum',
    '单价':'mean',
    '产品': 'count'
})
# 将结果按总销售额降序排列。
print(group.sort_values('销售额',ascending=False))
# 5. 分组统计（进阶）
# 使用 pivot_table 或 groupby，创建一张透视表，以 地区 为行，产品   为列，值为 销售额总和，并填入缺失值（例如填充 0）。
# 另外计算每个地区的总销售额（即行合计）和每个产品的总销售额（即列合计），并添加到透视表中（可手动添加或使用 margins=True）。
# 6. 日期维度分析
# 提取 月份（假设所有日期在同一年），按月份分组，统计每月的总销售额和总销量。
DataFrame['月']=DataFrame['日期'].dt.strftime('%m')
print(DataFrame)
group_m=DataFrame.groupby('月',as_index=False).agg({
    '销售额':'sum',
    '销量':'sum'
})
print(group_m)
# 按月份绘制简单的折线图（可选，鼓励使用 matplotlib 或 seaborn 进行可视化）。
# 7. 保存结果到 Excel 文件
# 将以下内容分别写入同一个 Excel 文件 sales_report.xlsx 的不同 sheet 中：
# Sheet1: 原始清洗后的完整数据（包括新增的“销售额”列）
with pd.ExcelWriter("DataFrame.xlsx",engine="xlsxwriter") as writer:
    a.to_excel(writer, sheet_name = "Sheet1", index = False)
# Sheet2: 按产品分组统计结果（任务4的结果）
    group.to_excel(writer, sheet_name = "Sheet2")
# Sheet3: 按地区×产品的透视表（任务5的结果）
# Sheet4: 按月统计结果（任务6的结果）
    group_m.to_excel(writer, sheet_name = "Sheet4")
# 确保 Excel 文件格式规范（如列宽自适应、数字格式等），至少要求保存成功。