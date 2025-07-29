import itertools
import time

def knapsack_bruteforce(weights, values, max_weight):
    n = len(weights)
    max_value = 0
    best_combination = []

    # Test all possible combinations
    for i in range(1, n + 1):
        for combination in itertools.combinations(range(n), i):
            total_weight = sum(weights[j] for j in combination)
            total_value = sum(values[j] for j in combination)

            if total_weight <= max_weight and total_value > max_value:
                max_value = total_value
                best_combination = combination

    return max_value, best_combination

# Test the algorithm
weights = [10, 20, 30] # the weights for each pakages,
values = [60, 100, 120] # values starting from 3 to 52 (just as an example)

max_weight = 50

start_time=time.time()
max_value, best_combination = knapsack_bruteforce(weights, values, max_weight)
end_time=time.time()

excution_time=end_time-start_time
print(f"Maximum possible value: {max_value}")
print(f"Best combination of items: {best_combination}")
print(f"Excution time:{excution_time} seconds")
