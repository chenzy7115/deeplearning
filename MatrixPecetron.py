import numpy as np

# x = np.array([0, 1])
# w = np.array([0.5, 0.5])
# b = -0.7
# tem = w * x

# print(tem)

# print(np.sum(tem))

# print(np.sum(tem) + b)
# 上面的代码是perceptron的实现数学原理，下面的代码是perceptron的实现


def AND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(W * X) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(W * X) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(W * X) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 所有的pecetron都是相同的，不同的只是权重和偏置值
# 下面为输出结果展示
print("AND Gate 的计算结果为,输入的都是(0,0)(1,0)(0,1)(1,1):")
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

print("OR Gate 的计算结果为,输入的都是(0,0)(1,0)(0,1)(1,1):")
print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))

print("NAND Gate 的计算结果为,输入的都是(0,0)(1,0)(0,1)(1,1):")
print(NAND(0, 0))
print(NAND(1, 0))
print(NAND(0, 1))
print(NAND(1, 1))
