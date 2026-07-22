import pandas as pd
import numpy as np
import os
import sys
import datetime
import matplotlib.pyplot as plt

filepath = "./sales.csv"
excelFile = "胡宇平-sales_report.xlsx"


def readData(filepath):
    df = pd.read_csv(filepath)
    print(df.head())
    print(df.info())
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(how="all")
    df = df.dropna(subset=["产品"])
    df["日期"] = df["日期"].fillna(datetime.datetime.now().strftime(f"%Y-%m-%d"))
    df["地区"] = df["地区"].fillna("北区")
    df["销量"] = df["销量"].fillna(0)
    df["单价"] = df["单价"].fillna(0)
    df["日期"] = pd.to_datetime(df["日期"])
    df["销售额"] = df["销量"] * df["单价"]
    df["产品"] = df["产品"].astype("category")
    print(df)
    print(df.info())
    return df


def dataSort(df: pd.DataFrame):
    df = df[df["销售额"] > 1500]
    df = df.sort_values(by="日期", ascending=True)
    print(df)
    return df


def group(df: pd.DataFrame):
    df = df.groupby("产品", as_index=False).agg(
        总销量=("销量", "sum"),
        总销售额=("销售额", "sum"),
        平均单价=("单价", "mean"),
        记录条数=("产品", "count"),
    )
    df = df.sort_values(by="总销售额", ascending=False)
    print(df)
    return df


def advanceGroup(df: pd.DataFrame):
    df = pd.pivot_table(
        df,
        values="销售额",
        index="地区",
        columns="产品",
        aggfunc="sum",
        fill_value=0,
        margins=True,
    )
    print(df)
    return df


def dateAnalyse(df: pd.DataFrame):
    df["月份"] = df["日期"].dt.to_period("M")
    df = df.groupby("月份", as_index=False).agg(
        每月总销售额=("销售额", "sum"), 每月总销量=("销量", "sum")
    )
    print(df)
    plt.figure(figsize=(8, 4))
    plt.plot(
        df["月份"].astype(str), df["每月总销售额"], marker="o", label="每月总销售额"
    )
    plt.title("每月销售额趋势")
    plt.xlabel("月份")
    plt.ylabel("销售额")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return df


def writeExcel(file):
    res1 = preprocess(readData(filepath))
    res2 = group(res1)
    res3 = advanceGroup(res1)
    # print(res1)
    res4 = dateAnalyse(res1)
    with pd.ExcelWriter(file) as writer:
        res1.to_excel(writer, sheet_name="Sheet1", index=False)
        res2.to_excel(writer, sheet_name="Sheet2", index=False)
        res3.to_excel(writer, sheet_name="Sheet3", index=False)
        res4.to_excel(writer, sheet_name="Sheet4", index=False)


if __name__ == "__main__":
    """res1 = preprocess(readData(filepath))
    res2 = dataSort(res1)
    group(res1)
    advanceGroup(res1)
    print(res1)
    dateAnalyse(res1)"""
    writeExcel(excelFile)
