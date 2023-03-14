# Midterm exam study guide

# Midterm logistics:

# Two-part exam: multiple-choice knowledge questions, followed by problem solving
# ~20 min. Multiple-choice will be short-timed and expect you to know answers without looking up.
# ~60 min. Problem solving will be open-book/google, so expect slightly more involved questions that require spending time.
#          There may be some existing that you can complete.

# The midterm exam will include all the topics we did so far:

# Python basics
# Advanced data structures: Collections, Dictionary, Set, Tuple, Slicing
# Exceptions
# Recursion
# OOP


# Knowledge questions will be on all previous quiz contents, plus:

# Exceptions
# Recursion
# Inheritance and Polymorphism
# Decorators
# Abstract classes
# Method overriding


# Problem questions will be on:

# Python basics: functions, control statements
# Using different data structures
# Proper use of exceptions
# Simple problem solving with recursion
# Building object oriented programs

vowels = [3, 5,3,6,7,8,0]

# sort the vowels
vowels.sort(reverse=False)


# print vowels
print('Sorted list (in Descending):', vowels)

print(set([1,2,3,6,7,1,3,8]))




from collections import Counter
words = "a word in a sentence".split(" ")
a_counter = Counter(words)

print(a_counter)

# This will count each word and display how many time it is in words.
# For example (Counter({'a': 2, 'word': 1, 'in': 1, 'sentence': 1}))