def knapsack(weights, values, capacity, index):
    # This is the base case , if we go thrgouth all pakages index = -1 end of list
    # or capacity is full  capacity =  0
    if index == -1 or capacity == 0:
        return 0

    # If weight of current package is  more then capacity , no need to complate skip to next package ,
    # like if you have a truck and you want to load it in other smaller track , it can not be and no need to look solution
    if weights[index ] > capacity:
        return knapsack(weights, values, capacity, index - 1)

    # case 1 - exclude
    exclude = knapsack(weights, values, capacity, index - 1)

    # case 2 - include
    include = values[index ] + knapsack(weights, values, capacity - weights[index ], index - 1)

    # Return the max of include and exclude , more : it will be like tree until it reach base case
    # then cacluate max as from bottom to up the tree
    return max(include, exclude)

# input example
weights = [10, 20, 30] # the weights for each pakages,
values = [60, 100, 120] # the values for each pakages,
capacity = 50  # maxaimum capacity
indexes = len(weights) - 1            # indexes start for top 2 to last one 0  in this example

# Call the knapsack function
max_value = knapsack(weights, values, capacity, indexes)
print("Maximum value that can be obtained:", max_value)
