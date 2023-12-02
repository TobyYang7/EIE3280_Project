import numpy as np
import matplotlib.pyplot as plt

# 参数设置
n_phases = 5  # 阶段数
n_iterations = 10  # 每个阶段的迭代次数
n_sites = 2  # 网站数量
n_strategies = 2  # 策略数量 (关键词优化和高质量内容)
epsilon = 0.1  # 随机性强度
gamma = 1.0  # 策略适应度参数
delta = 1.0  # 策略偏离成本参数
beta = 0.5  # 互动效应参数

# 初始化策略和效用
strategies = np.random.rand(n_phases, n_sites, n_strategies)
utilities = np.zeros((n_phases, n_sites))

# 模拟过程
for phase in range(n_phases):
    for iteration in range(n_iterations):
        for site in range(n_sites):
            # 对手的策略
            opponent_strategy = strategies[phase, 1-site, :]

            # 计算当前策略的效用
            utility = np.log(
                1 + beta * opponent_strategy[0]) - gamma * np.linalg.norm(strategies[phase, site, :] - 0.5)
            utilities[phase, site] = utility

            # 动态策略调整
            strategies[phase, site, :] += epsilon * \
                (np.random.rand(n_strategies) - 0.5)

# 可视化结果
phases = np.arange(1, n_phases + 1)
plt.figure(figsize=(12, 6))

# 绘制网站A的策略变化
plt.subplot(1, 2, 1)
plt.plot(phases, strategies[:, 0, 0], label='关键词优化 - 网站A')
plt.plot(phases, strategies[:, 0, 1], label='高质量内容 - 网站A')
plt.title('网站A的策略变化')
plt.xlabel('阶段')
plt.ylabel('策略强度')
plt.legend()

# 绘制网站B的策略变化
plt.subplot(1, 2, 2)
plt.plot(phases, strategies[:, 1, 0], label='关键词优化 - 网站B')
plt.plot(phases, strategies[:, 1, 1], label='高质量内容 - 网站B')
plt.title('网站B的策略变化')
plt.xlabel('阶段')
plt.ylabel('策略强度')
plt.legend()

plt.tight_layout()
plt.show()
