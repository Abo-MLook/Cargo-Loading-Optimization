import time

# Native recursive knapsack (no memoization)
def knapsack(weights, values, capacity, index):
    if index == -1 or capacity == 0:
        return 0, []

    if weights[index] > capacity:
        return knapsack(weights, values, capacity, index - 1)

    exclude_values, exclude_subset = knapsack(weights, values, capacity, index - 1)
    include_values, include_subset = knapsack(weights, values, capacity - weights[index], index - 1)
    include_values += values[index]
    include_subset += [index]

    if exclude_values > include_values:
        return exclude_values, exclude_subset
    else:
        return include_values, include_subset

# ==== Test input ====
n = 20 # native version will be slow here
capacity = 1000
weights = [1] * n
values = [1] * n
index = n - 1

# ==== Measure time ====
start_time = time.time()
max_value, selected_items = knapsack(weights, values, capacity, index)
end_time = time.time()

# ==== Output ====
print(f"Max Value: {max_value}")
print(f"Execution Time: {end_time - start_time:.10f} seconds")
