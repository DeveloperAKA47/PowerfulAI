"""numpy_ai_homework.py

NumPy AI 基础算子实现作业（建议完成时间：4.5 小时）。

开发目标
--------
实现本文件中声明的 11 个公开 API。只允许使用 NumPy 和 Python 标准库，
不得使用 PyTorch、TensorFlow、JAX、SciPy、scikit-learn 或 pandas。

开发规则
--------
1. 不得修改公开函数的名称、参数顺序、默认值和返回值含义。
2. 输入通常应先通过 ``np.asarray`` 转换为 ``np.ndarray``。
3. 核心数组计算应使用 NumPy 向量化；不得用 Python 循环逐元素计算。
4. 参数类型错误应抛出 ``TypeError``；参数取值错误应抛出 ``ValueError``；
   数组形状不符合接口要求时应抛出 ``ShapeError``。
5. ``dtype=None`` 时，``one_hot`` 默认使用 ``np.float32``。
6. ``eps=None`` 时，``normalize`` 和 ``cosine_similarity`` 默认使用 ``1e-7``。
7. 浮点结果应考虑除零、指数溢出和舍入误差等数值稳定性问题。

说明
----
类型标注主要用于 IDE 提示、静态类型检查和接口阅读，并不会自动完成运行时校验。
成员仍需在函数体中显式编写必要的类型、范围和形状检查。
"""

from __future__ import annotations
import re
from typing import Any, Literal, TypeAlias

import numpy as np

__version__ = "0.1.0-homework"

__all__ = [
    "one_hot",
    "l2_norm",
    "normalize",
    "cosine_similarity",
    "pairwise_squared_distance",
    "relu",
    "leaky_relu",
    "sigmoid",
    "softmax",
    "mse_loss",
    "mae_loss",
]


# ---------------------------------------------------------------------------
# Public type aliases
# ---------------------------------------------------------------------------

# 可以被 np.asarray(...) 转换为数组的数据，例如：
# Python 标量、列表、元组以及 np.ndarray。
ArrayLike: TypeAlias = Any

# axis 可以是：
# - 一个整数，例如 -1、0、1；
# - 多个轴组成的元组，例如 (0, 1)；
# - None，表示不限定某个轴，而是处理全部元素。
AxisLike: TypeAlias = int | tuple[int, ...] | None

# 损失函数只允许三种归约方式。
Reduction: TypeAlias = Literal["none", "mean", "sum"]


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------


class NumPyAIError(Exception):
    """本模块异常的基类。"""


class ShapeError(NumPyAIError, ValueError):
    """当数组形状不符合接口约定时抛出。"""


# ---------------------------------------------------------------------------
# Encoding and vector operations
# ---------------------------------------------------------------------------
def word_statistics(text: str) -> dict[str, int]:
    t = {}
    text = text.strip()
    text = text.lower()
    wordRe = re.compile(r"\b\w+?\b")
    l = wordRe.findall(text)
    for i in l:
        t[i] = t.get(i, 0)
        t[i] += 1
    t = {k: v for k, v in t.items() if v >= 2}
    return t


def one_hot(
    indices: ArrayLike,
    num_classes: int,
    *,
    dtype: Any | None = None,
) -> np.ndarray:
    """把整数类别编号转换成独热编码数组。

    参数：
        indices:
            整数类别编号，可以是标量、列表、元组或 NumPy 数组。
        num_classes:
            类别总数，必须是正整数。所有类别编号必须位于
            ``[0, num_classes)`` 范围内。
        dtype:
            输出数组的数据类型。为 None 时使用 ``np.float32``。
            该参数位于 ``*`` 后面，调用时必须写成 ``dtype=...``。

    返回：
        形状为 ``indices.shape + (num_classes,)`` 的 NumPy 数组。

    示例：
        ``one_hot([2, 0, 1], 3)`` 的结果应等价于：
        ``[[0, 0, 1], [1, 0, 0], [0, 1, 0]]``。

    建议使用：
        ``np.asarray``、``np.issubdtype``、``np.integer``、``np.zeros``、
        ``np.arange``、``reshape`` 和高级索引。
    """

    array = np.asarray(indices)
    if not np.issubdtype(array.dtype, np.integer):
        raise TypeError("indices should be int")
    if num_classes <= 0:
        raise ValueError("num_classes must > 0")

    if array.size and (np.any(array < 0) or np.any(array >= num_classes)):
        raise ValueError("")
    np.astype()


def l2_norm(
    value: ArrayLike,
    *,
    axis: AxisLike = None,
    keepdims: bool = False,
) -> np.ndarray:
    """计算数组的 L2 范数。

    L2 范数可理解为：先逐元素平方，再求和，最后开平方。
    对向量 ``[3, 4]`` 计算应得到 ``5``。

    参数：
        value: 输入数据。
        axis: 沿哪个轴计算；None 表示对全部元素计算。
        keepdims: 是否保留被归约的维度。

    建议使用：
        ``np.asarray``、``astype``、``np.sum``、``np.sqrt``。
        也可以使用 ``np.linalg.norm``，但仍需处理输入类型。
    """
    raise NotImplementedError("TODO: implement l2_norm")


def normalize(
    value: ArrayLike,
    *,
    axis: AxisLike = -1,
    eps: float | None = None,
) -> np.ndarray:
    """沿指定轴进行 L2 归一化。

    核心含义是：``输出 = 输入 / 输入的 L2 范数``。
    对 ``[3, 4]`` 归一化后应得到约 ``[0.6, 0.8]``。

    ``eps`` 用来防止分母为 0；为 None 时使用 ``1e-7``。
    ``eps`` 必须是有限的正数。计算范数时通常需要
    ``keepdims=True``，以便利用广播完成除法。

    建议复用：
        ``l2_norm``。

    建议使用：
        ``np.maximum`` 和 NumPy 广播。
    """
    raise NotImplementedError("TODO: implement normalize")


def cosine_similarity(
    x: ArrayLike,
    y: ArrayLike,
    *,
    axis: int = -1,
    eps: float | None = None,
) -> np.ndarray:
    """计算两个数组沿指定轴的余弦相似度。

    核心含义是：
        点积 /（x 的 L2 范数 * y 的 L2 范数）

    两个输入必须能够按照 NumPy 广播规则共同计算；否则应抛出
    ``ShapeError``。``eps`` 为 None 时使用 ``1e-7``，用于防止除零。

    典型结果：
        方向相同约为 1；方向相反约为 -1；互相垂直约为 0。

    建议使用：
        ``np.broadcast_arrays``、``np.sum``、``np.maximum``，并复用
        ``l2_norm``。
    """
    raise NotImplementedError("TODO: implement cosine_similarity")


def pairwise_squared_distance(x: ArrayLike, y: ArrayLike) -> np.ndarray:
    """计算两组向量之间两两对应的平方欧氏距离。

    输入约定：
        ``x.shape == (m, d)``
        ``y.shape == (n, d)``

    输出约定：
        返回形状为 ``(m, n)`` 的数组；第 i 行第 j 列表示
        ``x[i]`` 与 ``y[j]`` 之间的平方距离。

    两个输入都必须是二维数组，并且特征维度 d 必须相同；否则抛出
    ``ShapeError``。

    必须使用向量化矩阵运算，不得编写双重 Python 循环。

    可使用的恒等式：
        ``||x-y||^2 = ||x||^2 + ||y||^2 - 2(x·y)``

    建议使用：
        ``np.sum``、``keepdims=True``、转置 ``.T``、矩阵乘法 ``@``、
        ``np.maximum``。
    """
    raise NotImplementedError("TODO: implement pairwise_squared_distance")


# ---------------------------------------------------------------------------
# Activation functions
# ---------------------------------------------------------------------------


def relu(value: ArrayLike) -> np.ndarray:
    """计算 ReLU：负数变为 0，非负数保持不变。

    必须使用 NumPy 向量化实现，不得逐元素循环。

    建议使用：
        ``np.asarray``、``np.maximum``。
    """
    raise NotImplementedError("TODO: implement relu")


def leaky_relu(
    value: ArrayLike,
    negative_slope: float = 0.01,
) -> np.ndarray:
    """计算 Leaky ReLU。

    当元素大于等于 0 时输出原值；小于 0 时输出
    ``negative_slope * value``。``negative_slope`` 不得小于 0。

    建议使用：
        ``np.asarray``、``np.where``。
    """
    raise NotImplementedError("TODO: implement leaky_relu")


def sigmoid(value: ArrayLike) -> np.ndarray:
    """计算数值稳定的 Sigmoid。

    数学形式为 ``1 / (1 + exp(-x))``，但直接使用该公式处理很大的
    负数时可能发生指数溢出。实现时应分别处理 ``x >= 0`` 和 ``x < 0``
    两个区域，并保证 ``[-1000, 0, 1000]`` 的输出全部为有限值。

    建议使用：
        ``np.asarray``、``astype``、``np.empty_like``、``np.exp``、
        布尔索引。
    """
    raise NotImplementedError("TODO: implement sigmoid")


def softmax(value: ArrayLike, *, axis: int = -1) -> np.ndarray:
    """沿指定轴计算数值稳定的 Softmax。

    输出沿 ``axis`` 的总和应约等于 1。为了避免 ``np.exp`` 溢出，
    应先让输入减去沿该轴的最大值，再计算指数和归一化。

    零维数组没有可计算的轴，应抛出 ``ShapeError``。

    建议使用：
        ``np.asarray``、``np.max``、``np.exp``、``np.sum``，并在归约时
        使用 ``keepdims=True``。
    """
    raise NotImplementedError("TODO: implement softmax")


# ---------------------------------------------------------------------------
# Loss functions
# ---------------------------------------------------------------------------


def mse_loss(
    prediction: ArrayLike,
    target: ArrayLike,
    *,
    reduction: Reduction = "mean",
) -> np.ndarray | float:
    """计算均方误差损失（Mean Squared Error）。

    逐元素损失：``(prediction - target) ** 2``。

    ``reduction`` 只允许：
        ``"none"``：返回逐元素损失数组；
        ``"sum"``：返回所有损失之和；
        ``"mean"``：返回所有损失的平均值。

    prediction 与 target 可以按照 NumPy 广播规则计算；如果无法广播，
    应把 NumPy 的 ``ValueError`` 转换为 ``ShapeError``。

    建议使用：
        ``np.asarray``、数组减法、平方、``np.sum``、``np.mean``。
    """
    raise NotImplementedError("TODO: implement mse_loss")


def mae_loss(
    prediction: ArrayLike,
    target: ArrayLike,
    *,
    reduction: Reduction = "mean",
) -> np.ndarray | float:
    """计算平均绝对误差损失（Mean Absolute Error）。

    逐元素损失：``abs(prediction - target)``。

    ``reduction`` 的规则与 ``mse_loss`` 相同。建议将两者共有的
    reduction 校验和处理逻辑抽取为私有辅助函数，但不得修改公开接口。

    建议使用：
        ``np.asarray``、``np.abs``、``np.sum``、``np.mean``。
    """
    raise NotImplementedError("TODO: implement mae_loss")


if __name__ == "__main__":
    res = word_statistics("Python is good, Python is easy. Good code is important!")
    print(res)
