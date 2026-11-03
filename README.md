# 深度学习入门学习项目

本项目用于学习《深度学习入门：基于 Python 的理论与实现》，包含**教材配套的官方源代码**以及**个人编写的练习脚本**。通过手动实现感知机、神经网络、梯度下降、卷积网络等经典模型，帮助理解深度学习背后的数学原理与工程实现。

## 项目结构

```
deeplearning/
├── MatrixPecetron.py        # 个人练习：感知机(Perceptron)矩阵实现（AND/OR/NAND 门）
├── perception.py            # 个人练习：感知机基础实现（权重+阈值）
├── drawSin.py               # 个人练习：matplotlib 绘制 sin/cos 函数图
├── showImage.py             # 个人练习：读取并显示 lena.png 图片
├── showNumpy.py             # 个人练习：NumPy 基本用法
├── test.py / testNumpy.py   # 测试脚本
├── conda-vscode-guide.html  # conda + VSCode 环境配置说明
├── man.py / lena.png        # 示例图片与脚本
└── book/                    # 教材配套源码
    ├── ch01  Python 入门
    ├── ch02  感知机
    ├── ch03  神经网络
    ├── ch04  神经网络的学习
    ├── ch05  误差反向传播法
    ├── ch06  与学习相关的技巧
    ├── ch07  卷积神经网络
    ├── ch08  深度学习
    ├── common/    # 公共模块（层、优化器、训练器等）
    ├── dataset/   # MNIST 等数据集加载
    ├── README.md
    └── LICENSE.md
```

## 环境依赖

- Python 3.x
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)

安装依赖：

```bash
pip install numpy matplotlib
```

## 快速体验

运行感知机门电路示例：

```bash
python MatrixPecetron.py
```

绘制 `sin/cos` 函数曲线：

```bash
python drawSin.py
```

显示示例图片：

```bash
python showImage.py
```

## 内容说明

### 感知机（Perceptron）

感知机接收多个输入信号，输出一个信号，是神经网络（多层感知机）的基础单元。本项目通过 `AND`、`OR`、`NAND` 逻辑门的实现，验证感知机对线性可分问题的分类能力。

> 提示：`NAND` 门是 `AND` 门的取反，实现时需要将权重取反（`W = [-0.5, -0.5]`），否则 `NAND(1,1)` 会输出错误结果。

### 教材配套源码

`book/` 目录下是基于《深度学习入门》一书，按章节组织的示例代码，涵盖从感知机到卷积神经网络（CNN）的完整学习路径，并包含通用的网络层、优化器与训练器实现，适合按章节循序渐进学习。

## 参考

- 书籍《深度学习入门：基于 Python 的理论与实现》（斋藤康毅 著）
- 教材配套源码与高清 PDF 见 `book/` 目录