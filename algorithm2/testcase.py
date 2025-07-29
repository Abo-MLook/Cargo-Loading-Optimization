import time


# Bottom-up DP implementation of the 0/1 Knapsack Problem
def knapsackDP(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ==== Test input ====
n = 6
capacity = 100
weights = [1] * n
values = [1] * n

# ==== Measure time ====
start_time = time.time()
max_value = knapsackDP(weights, values, capacity)
end_time = time.time()

# ==== Output ====
print(f"Max Value: {max_value}")
print(f"Execution Time: {end_time - start_time:.10f} seconds")
