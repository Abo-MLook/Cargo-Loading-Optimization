def knapsack_recursive(weights, values, capacity, index):
    # Base case: if no items left or the capacity is full
    if index == 0 or capacity == 0:
        return 0

    # If weight of the current package is more than the remaining capacity, exclude it
    if weights[index - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, index - 1)

    # Option 1: Exclude the current package
    exclude = knapsack_recursive(weights, values, capacity, index - 1)

    # Option 2: Include the current package (if it fits)
    include = values[index - 1] + knapsack_recursive(weights, values, capacity - weights[index - 1], index - 1)

    # Return the maximum of both options (include or exclude)
    return max(include, exclude)

# Example usage:
weights = [10, 20, 30]  # Weights of the packages
values = [60, 100, 120]  # Values of the packages
capacity = 50  # Maximum weight capacity of the truck
n = len(weights)

# Call the knapsack function
max_value = knapsack_recursive(weights, values, capacity, n)
print("Maximum value that can be obtained:", max_value)
