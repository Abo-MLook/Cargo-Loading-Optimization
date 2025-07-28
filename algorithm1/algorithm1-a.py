import random
import time

# Memoization cache (dictionary) to store the results of subproblems
memo = {}

def knapsack(weights, values, capacity, index):
    # Base case: if we've gone through all packages (index = -1) or the capacity is full (capacity = 0)
    if index == -1 or capacity == 0:
        return 0, []  # Return 0 value and an empty list for the subset

    # Check if the result for this subproblem is already computed (in memo)
    if (index, capacity) in memo:
        return memo[(index, capacity)]  # Return the stored result if already computed

    # If the weight of the current package exceeds the remaining capacity, skip it
    if weights[index] > capacity:
        result = knapsack(weights, values, capacity, index - 1)
        memo[(index, capacity)] = result  # Store the result in the memo dictionary
        return result

    # Option 1: Exclude the current package
    exclude_values, exclude_subset = knapsack(weights, values, capacity, index - 1)

    # Option 2: Include the current package
    include_values, include_subset = knapsack(weights, values, capacity - weights[index], index - 1)
    include_values += values[index]  # Add the value of the included package
    include_subset += [index]  # Add the current package index to the list of selected items

    # Choose the best option (maximum value between include and exclude)
    if exclude_values > include_values:
        result = exclude_values, exclude_subset
    else:
        result = include_values, include_subset

    # Store the result in the memo dictionary for future reference
    memo[(index, capacity)] = result

    return result


# Generate a random test case with 3 packages
def generate_random_test_case(num_packages=30, max_capacity=1000000000000):
    # Generate random weights for each package (between 1 and 50)
    weights = [random.randint(1, 50) for _ in range(num_packages)]
    # Generate random values for each package (between 50 and 200)
    values = [random.randint(50, 200) for _ in range(num_packages)]
    # Generate random capacity for the truck (between 50 and max_capacity)
    capacity = random.randint(50, max_capacity)

    return weights, values, capacity

# Generate a random test case with 3 packages
weights, values, capacity = generate_random_test_case()

# Run the knapsack function and measure execution time
start_time = time.time()  # Start timer for performance measurement
max_value, optimal_solution_indexes = knapsack(weights, values, capacity, len(weights) - 1)
end_time = time.time()  # End timer

# Output the results

Execution_Time = end_time - start_time
print(f"Execution Time: {Execution_Time:.10f} seconds")
