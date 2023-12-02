import numpy as np
from scipy.optimize import minimize

# 假设
num_participants = 2  # 参与者数量
strategies = 2  # 每个参与者的策略数量

# 定义支付函数


def utility(player, strategies):
    # 简化的支付函数，这里只是一个示例
    u = np.log(1 + sum(strategies)) - np.linalg.norm(strategies[player] - 1)
    return u

# 优化目标函数


def objective(strategies):
    # 总支付函数的负值（因为minimize函数是找最小值）
    total_utility = -sum(utility(player, strategies)
                         for player in range(num_participants))
    return total_utility


# 初始策略
initial_strategies = np.random.rand(num_participants, strategies)
initial_strategies = np.array(initial_strategies).flatten()
# 执行优化
result = minimize(objective, initial_strategies, method='BFGS')

# 显示结果
optimal_strategies = result.x.reshape(num_participants, strategies)
print("最优策略:", optimal_strategies)
