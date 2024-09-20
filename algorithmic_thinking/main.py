# 1. Brute Force Algorithm
# try all possible candidate solutions called
# an example is linear search
# impractical time to solve
# insufficient as perform the same number of check as the length of array
def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")


# selection sort
# Find the smallest element in the array and exchange it with the first element position
# Find the second-smallest element in the array and exchange it with second element position and so on
# At each stage of selection sort, the list is partitioned into sorted and unsorted regions.
# pseudocode
# create a variable called min_idx and assign it a value of 0
# iterate through list if the current value is less than value at min_idx
# then update the min_idx to current idx
def find_min(xs):
    min_idx = 0
    current_idx = min_idx + 1
    for _ in enumerate(xs):
        if xs[current_idx] < xs[min_idx]:
            min_idx = current_idx
    return min_idx


xs_list = [3, 2, 1, 5, 4]
min_value = find_min(xs_list)
print(f"The minimum value is {min_value}.")


def selection_sort(xs):
    for i in range(len(xs) - 1):  # The last value will automatically be in correct position.
        # Find minimum value in unsorted region.
        min_index = i
        for j in range(i + 1, len(xs)):
            # Update min_index if the value at j is lower than current minimum value.
            if xs[j] < xs[min_index]:
                min_index = j
        # After finding the minimum value in the unsorted region, swap with the first unsorted value.
        xs[i], xs[min_index] = xs[min_index], xs[i]


xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))

# efficiency and complexity
# Efficient: time complexity and space (memory) complexity
# Time complexity of basic operation as a function of size of input
# Basic operation: assignments, arithmetic operation, comparison, return statement, and calling function
n = 100  # assignment
count = 0  # assignment
while count < n:  # comparison n times
    count += 1  # assignment n times + arithmetic n times
    print(count)  # output n time
# calculation of time complexity = 1 + 1 + n + n + n = 2 + 4n (time complexity is dependent on n)
# Big-O notation is away of expressing an upper bound on execution time or space requirement
# Big-omega is lower bound
# Big-theta is average
# Pass a certain point an algorithm will not be worse than it's upper bound (worse case scenario)
# How the algorithm performs with very large input
# calculating time complexity
# Count basic operation
# constant is ignored ie 2 + 4n = O(n)
# Ignore all but the largest term ie 500+n = O(n), sq(n)+400n+ 100 = O(n)
# classify which category

# minimize the complexity (linear, log, linear and so on)
# nested loop result in quadruple (O(n^nested loop number) time complexity, which is not ideal
for i in range(n):
    for j in range(n):
        print(i, j)


# complexity O(n^2)

# Space complexity
def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


# space complexity is O(1) constant since we are always going to have only those two variables

my_list = [5, 4, 3, 2, 1]
print(my_sum(my_list))


def double(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[i] * 2)
    return new_list


my_list = [5, 4, 3, 2, 1]
print(double(my_list))


# space complexity is O(n) linear, the longer the initial list (input) the longer new list

# 2. Greedy Algorithm
# make locally optimal choices and do not revisit choice once made
# change making example
def make_change(target_amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]  # Order is important!
    coin_count = 0  # Initialise count
    values = []  # Store values here
    for coin in denominations:
        while target_amount >= coin:  # Use the current coin until its value is too large
            target_amount -= coin  # Decrease the remaining amount
            values.append(coin)  # Make a note of which coin was used
            coin_count += 1  # Increase the coin count
    return coin_count, values


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p

# Dijkstra:
# use the shortest path in a weighted graph
# optimal
# weight must be positive to guarantee the correct result
# find the shorts path to every node from the origin
# pseudocode:
# distance can be any weighting such as time or cost or any other factors
# while a vertex remains unvisited
# visit unvisited vertex with the smallest distance from the start vertex (current_vertex)
# for each unvisited neighbour of current_vertex
# calculate the new distance from the start vertex if this route taken
# if the calculated distance of this vertex is less than the known distance
# update the distance for the neighbour

# This is a pythonic implementation just for understanding
# use https://networkx.org/ or other packages

# 3. Decrease and conquer
# at each step of the algorithm, the problem is reduced to a smaller version of the same problem until
# solution is found (or found not to be possible)
# decrease by constant or factor ie factor of 2 as in binary search or variable as in Euclidean algorithm
# Binary search
    # sorted data
    # assign pointers at first and last index in the list
    # calculate the midpoint = (lower bound index + upper bound index)//2
    # check if the value at midpoint index is the correct value
    # if not then move the lower bound index to midpoint + 1
    # time complexity is O(log n) but data have to be sorted and the best sor algorithm O(n log n)
    # binary search only make sense if data will be searched multiple times


def binary_search(data, target):
    lower_bound = 0
    upper_bound = len(data) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound)//2
        if data[midpoint] == target:
            return midpoint
        elif data[midpoint] < target:
            lower_bound = midpoint + 1
        else:
            lower_bound = midpoint - 1
    return -1


max_val = 100
data = [20, 15, 10, 30]
data.sort()
print("Data:", data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print("You target value has been found at index", target_pos)

