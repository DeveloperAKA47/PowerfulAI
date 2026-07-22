import pandas as pd
print(pd.__version__)
#1=================
df = pd.read_csv('sales.csv')
print(df.head())
print(df.info())
#2==================
print(df.isna())
#这不是无缺失吗？不处理
df['日期'] = pd.to_datetime(df['日期'])
df['销售额'] = df['销量'] * df['单价']
df['产品'] = df['产品'].astype('category')
#3============================
a = df[(df['销售额'] > 1500)]
print(a)
df = df.sort_values(by='日期')
print(df)
#4=========================
gr = df.groupby('产品').agg(
    总销量= ('销量','sum'),
    总销售额=('销售额','sum'),
    平均单价= ('单价','mean'),
    订单数=('产品','count')
)
print(gr)
gr = gr.sort_values(by='总销售额')
print(gr)
#5===========================
#pass
#6==========================
df['月份'] = df['日期'].dt.month
b = df.groupby('月份').agg(
    总销量= ('销量','sum'),
    总销售额=('销售额','sum')
)
print(b)
#7=========================
with pd.ExcelWriter('sales_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
    gr.to_excel(writer, sheet_name='Sheet2')
    b.to_excel(writer, sheet_name='Sheet4')






