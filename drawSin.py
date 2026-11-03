import matplotlib.pyplot as plt
import numpy as np

# ≪推荐≫ 设置中文字体（黑体），并解决负号显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 指定黑体显示中文
plt.rcParams["axes.unicode_minus"] = False  # 解决负号 "-" 显示为方块

x = np.arange(0, 6, 0.2)
y = np.sin(x)
plt.plot(x, y)
plt.plot(x, np.cos(x))

plt.xlabel("x轴")
plt.ylabel("y轴")
plt.grid(True)

plt.legend(
    ["sin", "cos"],
    loc="upper right",
    fontsize=10,
    frameon=True,
    shadow=True,
    ncol=2,
    title="函数",
)
plt.show()
