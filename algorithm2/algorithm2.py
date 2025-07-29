def knapsackDP(weights, values, capacity):
    n = len(weights)

    # Create a 2D DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find selected items
    selected_indexes = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_indexes.append(i - 1)
            w -= weights[i - 1]


    return dp[n][capacity], selected_indexes


# === Input example ===
weights = [10, 20, 30]       # Weights for each package
values = [60, 100, 120]      # Corresponding values
capacity = 50                # Max capacity of the knapsack

# === Function call ===
max_value, selected_indexes = knapsackDP(weights, values, capacity)

# === Output results ===
print("The optimal Solution (DP):\n")
for i in selected_indexes:
    print(f"Pakage {i+1} : {weights[i]} weight  ||  ${values[i]} value", end="\n----\n")
print(f"======\nTotal = ${max_value}")
