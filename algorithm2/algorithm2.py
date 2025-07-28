def knapsackDP(weights, values, capacity):
    n = len(weights)  # Length of weights

    # Create a 2D array to store the partial values. dp[i][w] is the best value for capacity w using the first i items.
    dp = [[0] * (capacity + 1)] * (n + 1)  # Initialize dp table with 0s
    # Loop through the items
    for i in range(1, n + 1):
        # Loop through the capacity
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If the item can be included in the knapsack
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]  # Include the item
                exclude = dp[i - 1][w]  # Exclude the item
                dp[i][w] = max(include, exclude)  # Choose the better value between including and excluding
            else:
                dp[i][w] = dp[i - 1][w]  # If the item cannot be included (its weight is greater than the current capacity)

    # return the optimal value that can be achieved with the full capacity
    return dp[n][capacity]

# Input examples
weights = [10, 20, 30]  # Weights
values = [60, 100, 120]  # Values
capacity = 50  # Max capacity

# print the output
print(knapsackDP(weights, values, capacity))
