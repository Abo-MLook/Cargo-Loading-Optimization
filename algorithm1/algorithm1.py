def knapsack(weights, values, capacity, index):
    # Base case: if no items left or the capacity is full
    if index == -1 or capacity == 0:
        return 0

    # If weight of the current package is more than the remaining capacity, exclude it
    if weights[index ] > capacity:
        return knapsack(weights, values, capacity, index - 1)

    # Option 1: Exclude the current package
    exclude = knapsack(weights, values, capacity, index - 1)

    # Option 2: Include the current package (if it fits)
    include = values[index ] + knapsack(weights, values, capacity - weights[index ], index - 1)

    # Return the maximum of both options (include or exclude)
    return max(include, exclude)

# input example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
indexes = len(weights) - 1

# Call the knapsack function
max_value = knapsack(weights, values, capacity, indexes)
print("Maximum value that can be obtained:", max_value)
