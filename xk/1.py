import numpy as np
import matplotlib.pyplot as plt

# 定义地图大小和时间步长
N = 100  # 地图大小
T = 1000  # 时间步长

# 定义黄蜂初始位置
x = np.zeros((N, N), dtype=int)
x[N//2, N//2] = 1

# 定义移动概率矩阵
p = np.array([[0, 0.25, 0], [0.25, 0, 0.25], [0, 0.25, 0]])

# 模拟黄蜂扩散
for t in range(T):
    # 对每个黄蜂进行随机移动
    for i in range(N):
        for j in range(N):
            if x[i, j] == 1:
                # 随机选择移动方向
                d = np.random.choice([-1, 0, 1], size=2, p=p.flatten())
                # 计算新位置
                i_new = i + d[0]
                j_new = j + d[1]
                # 检查新位置是否越界
                if i_new >= 0 and i_new < N and j_new >= 0 and j_new < N:
                    # 移动黄蜂
                    x[i, j] = 0
                    x[i_new, j_new] = 1

# 绘制黄蜂扩散图
plt.imshow(x, cmap='gray')
plt.title('Bee diffusion after {} time steps'.format(T))
plt.show()
