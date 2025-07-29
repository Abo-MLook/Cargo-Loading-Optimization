def knapsackDP(weights, values, capacity):
    n = len(weights)  # Number of packages/items

    # step 1: Create a 2D table (rows: items, columns: capacity)
    # dp[i][w] will store the best total value for the first i items with max weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Step 2: Fill the table from top-left to bottom-right
    # This is bottom-up dynamic programming approach
    for i in range(1, n + 1):  # Go through each item one by one
        for w in range(1, capacity + 1):  # Go through each capacity value
            if weights[i - 1] <= w:
                # Case 1: Include the item if it fits
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Case 2: Exclude the item
                exclude = dp[i - 1][w]
                # Take the maximum of both choices
                dp[i][w] = max(include, exclude)
            else:
                # If item doesn't fit, just carry forward the previous value
                dp[i][w] = dp[i - 1][w]

    # Step 3: Backtrack from dp[n][capacity] to find which items were included
    selected_indexes = []
    w = capacity  # Start from full capacity
    for i in range(n, 0, -1):  # Go backwards from last item
        if dp[i][w] != dp[i - 1][w]:
            # This means item i-1 was included
            selected_indexes.append(i - 1)
            w -= weights[i - 1]  # Reduce the remaining capacity



    # Return the best total value and the indexes of items used
    return dp[n][capacity], selected_indexes


# inputs:
weights = [10, 20, 30]       # the weights for each package
values = [60, 100, 120]      # the values for each package
capacity = 50                # maximum weight capacity the truck can carry

# call the dynamic programming knapsack function
max_value, selected_indexes = knapsackDP(weights, values, capacity)

# Print the selected packages
print("The optimal Solution (DP):\n")
for i in selected_indexes:
    print(f"Pakage {i+1} : {weights[i]} weight  ||  ${values[i]} value", end="\n----\n")
print(f"======\nTotal = ${max_value}")
