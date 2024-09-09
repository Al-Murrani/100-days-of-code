# https://medium.com/data-bistrot/python-tips-and-tricks-for-efficient-coding-81b3c0195410

from collections import Counter
from datetime import datetime
import inspect
import random
import re

# list comprehension, [expression for item in iterable if condition]
numbers = [1, 3, 4, 5]
list_comprehension = [num * 2 for num in numbers if num > 3]
print(list_comprehension)
# iterating over dictionary
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
ages = [person["age"] for person in data if person["age"] > 25]
print(ages)
# flattening a matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

# Underscore (_)
# 1. Last Expression in Python Interpreter
# 2. Ignoring Values
filename, _ = 'example.txt'.split('.')
print(filename)
# 3. As a Loop Variable, loop runs 5 times, but the index is irrelevant
for _ in range(5):
    print("Hello, World!")
# 4. Formatting Large Numbers
amount = 1_000_000
print(amount)
# 5. Placeholder for Temporary or Unimportant Variables
x, _, y = (1, 'ignored', 3)  # x = 1, y = 3
print(x, y)

# enumerate, iterating over sequences in Python, it’s common to need both the index and the value of each item.
# enumerate(iterable, start=0)
names = ['Alice', 'Bob', 'Cathy']
for index, name in enumerate(names):
    print(index, name)
#  modify elements in a list while iterating:
grades = [50, 70, 80]
for index, grade in enumerate(grades):
    grades[index] = grade + 5
print(grades)
# return items based on it's position
data = [100, 200, 300, 400, 500]
even_data = [datum for index, datum in enumerate(data) if index % 2 == 0]
print(even_data)

# zip , combine multiple iterables (like lists, tuples, or dictionaries) into a single iterable of tuples
# zip(iterable1, iterable2, ..., iterableN)
# Pairing Elements
names = ['Alice', 'Bob', 'Cathy']
ages = [25, 30, 35]
paired = list(zip(names, ages))
print(paired)
# Working with Multiple Iterables
ids = [1, 2, 3]
names = ['Alice', 'Bob', 'Cathy']
grades = ['A', 'B', 'A+']
students = list(zip(ids, names, grades))
print(students)
# Unzipping Values
zipped = zip(ids, names, grades)
unzipped = list(zip(*zipped))
print(unzipped)
# Practical Applications in Data Projects
keys = ['name', 'age', 'grade']
values = ['Alice', 25, 'A']
student_dict = dict(zip(keys, values))
print(student_dict)

# Sorting Complex Iterables, sorted()
# returns a new sorted list, be it lists, tuples, dictionaries, or even custom objects
# default ascending order
# sorted(iterable, key=None, reverse=False)
words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words)
print(sorted_words)
# Sorting with Custom Keys
data = ['a5', 'a2', 'b1', 'b3', 'c2']
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)
# Sorting Tuples by Specific Element
tuples = [(1, 'c'), (2, 'a'), (1, 'b')]
sorted_tuples = sorted(tuples, key=lambda z: z[1])
print(sorted_tuples)
# Reverse Sorting
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)
# practical example
employees = [
    {'name': 'Alice', 'age': 30, 'salary': 80000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 120000},
]
# Sort by age, then by salary if ages are the same
sorted_employees = sorted(employees, key=lambda x: (x['age'], x['salary']))
print(sorted_employees)


# from __future__ import statement in Python is a critical tool for developers aiming to use newer
# Python features in older versions of the interpreter
# Test future features
# Ease transition between Python versions
# Improve code consistency

# Generators with yield
# Reading Large Files
# Data Streaming
# Large Calculations
# memory efficiency and large dataset processing

# inspect module, standard utility module.  Usage: Debugging, Documentation, Dynamic Inspection
# Retrieving Source Code
# Inspecting Classes and Functions
# Working with the Call Stack
def sample_function():
    return "Inspect me!"


# 1. Get the source code
source_code = inspect.getsource(sample_function)
print(source_code)


# 2. list of function arguments
def greeter(name_, greeting="Hello"):
    print(f"{greeting}, {name_}!")


args = inspect.signature(greeter).parameters
print(args)

# 3. Checking if an Object is a Function
print(inspect.isfunction(greeter))


# 4. Retrieving Documentation
def my_function():
    """This is a docstring for my_function."""
    pass


docstring = inspect.getdoc(my_function)
print(docstring)


#  5. Examining the Call Stack
def who_called_me():
    for frame in inspect.stack():
        print(inspect.getframeinfo(frame[0]))


def caller():
    who_called_me()


caller()

# f string and formatting number
price = 49.99
formatted_price = f"The price is {price:.2f} dollars."
print(formatted_price)
# date formatting
current_date = datetime.now()
formatted_date = f"Today's date is {current_date:%B %d, %Y}."
print(formatted_date)

# if x in list
fruit = 'apple'
fruits = ['apple', 'banana', 'cherry']

if fruit in fruits:
    print("Fruit is in the list.")

# str.join(), str.split()
# delimiter.join(iterable_of_strings)
# string.split(separator=None, maxsplit=-1)

# Sets, use set or {}, usage testing for membership
# managing collections of items where uniqueness is a key requirement
# initialize a set with multiple elements that are the same, the set will automatically remove duplicates
# add() or remove() method
# Union
a = {1, 2, 3}
b = {4, 5, 2}
print(a | b)
# Intersection
print(a & b)
# Difference
print(a - b)

# Walrus Operator
# variable := expression
# Collecting user input until a blank line is entered
# lines = []
# while (line := input("Enter something (leave blank to quit): ")) != "":
# lines.append(line)
# Generating and filtering random numbers
# numbers = [n for _ in range(10) if (n := random.randint(1, 100)) > 50]
# print(numbers)
# Checking the length of a list and using it in the same condition
a = [1, 2, 3]
if (n := len(a)) > 2:
    print(f"The list is long enough ({n} elements).")

# dictionary comprehension
# {key_expression: value_expression for item in iterable if condition}
# lists to dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)
# Merging Dictionaries with the Double Asterisk (**)
# If overlapping keys, the values from the later dictionaries in the sequence overwrite those from the earlier ones.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
# conditional merging
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
# Merge with a condition, e.g., only keys that are vowels
merged_dict = {**{k: v for k, v in dict1.items() if k in 'aeiou'}, **{k: v for k, v in dict2.items() if k in 'aeiou'}}
print(merged_dict)

# collections module provides several convenient container data types
# Counter is a specialized dictionary designed to count occurrences of elements in an iterable
# frequency distribution of data
data = ['apple', 'orange', 'banana', 'apple']
count_data = Counter(data)

counter = Counter(apples=2, bananas=3, oranges=1)
print(counter['bananas'])
more_fruits = ['apple', 'grape', 'grape']
counter.update(more_fruits)
more_fruits = ['apple', 'grape', 'pear']
counter.update(more_fruits)
print(counter.most_common(2))

c1 = Counter(a=4, b=2, c=0, d=-2)
c2 = Counter(a=1, b=2, c=3, d=4)
# Addition
print(c1 + c2)  # Output: Counter({'a': 5, 'c': 3, 'b': 4, 'd': 2})
# Subtraction
print(c1 - c2)  # Output: Counter({'a': 3})
# Intersection
print(c1 & c2)  # Output: Counter({'a': 1, 'b': 2})
# Union
print(c1 | c2)  # Output: Counter({'a': 4, 'c': 3, 'b': 2, 'd': 4})

# Sample text
text = "Python is great. Python is dynamic. Python is popular."
# Tokenize the text (convert to lowercase to count all variations of the word)
words = re.findall(r'\b\w+\b', text.lower())
# Create a Counter object
word_count = Counter(words)
print(word_count)
