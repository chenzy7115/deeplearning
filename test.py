hungry = True
if hungry:
    print("I am hungry")

hungry = False
if hungry:
    print("I am hungry")
else:
    print("I am not hungry")
    print("I am sleep")

for i in [1, 2, 3, 4, 5]:
    print(i)


def hello():
    print("hello world")


hello()


def helloCat(object):
    """
    helloCat 函数用于向猫打招呼，并打印传入的对象内容。

    Args:
        object: 任意类型的对象，将被打印输出。

    Example:
        >>> helloCat("cat")
        hello cat
        cat
    """
    print("hello cat")
    print(object)


helloCat("cat")
