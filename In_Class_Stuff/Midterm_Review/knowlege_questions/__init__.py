# Knowledge questions will be on all previous quiz contents, plus:

# Exceptions
# Recursion
# Inheritance and Polymorphism
# Decorators
# Abstract classes
# Method overriding



# Question 1
# Write the code for creating a variable that contains a list with at least 5 items,
# then use slicing to return at least 2 items from the list that are not adjacent.
# Explain which items will be selected.
list = [1,2,3,4,5]
a = list[0:4:2]  # start, stop, step
print(a)


print()
# Define a Python function funk(x) that adds 2 to the input argument and returns it.
def funk(x):
    a = x + 2
    return a

print(funk(9))


print()
# Let's say we want to access the "read_csv" function in the pandas library. How can we access this function if we use the statement
# import pandas as pd
# ?
# Answer = pd.read_csv(...)


# Write an example for a simple for-loop in Python and show the expected output.
list = [0,1,2,3,4]
for i in list:
    print(i)

# output: 0,1,2,3,4


# Which is NOT proper comment in Python?
# Answer = % followed by text


# Write a Python list that contains the values from 1 to 3. Do not use a variable, just write the list.
list_A = [1,2,3]


# Which is NOT possible using dictionaries in Python?
# Answer = Storing duplicate keys


# Which of the following is NOT a proper quotation in Python?
# Answer = 'Let's do this!'


print()
#Which of the following is a correct if statement in Python?
if a == 1:
    print("yes, it's one.")
elif a == 2:
    print("no, it's two.")
else:
    print("it's neither.")


# What is the resulting value in variable "a" after executing:
# a = 1 if False else True
# Answer= True


print()
# What should be in the list variable, a_9, for the following program to print "hello"?
a_9 = False
if not a_9:
    print("hello")


print()
# Complete the ... line below with a sorting statement such that the next line prints the list sorted from high to low:
a_list = [1,3,2]
a_list.sort()
print(a_list)


print()
#What would be the output of the following program:
for a in range(5):
    if a == 2:
        continue
    if a == 1:
        break
    print(a)
# Answer = 0



# Which is NOT possible using dictionaries in Python?
# Answer = Storing duplicate keys


print()
# What would be the contents of the following set:
print(set([1,2,3,6,7,1,3,8]))
# Answer = {1, 2, 3, 6, 7, 8}


# What would be the zip statement to result in the following output:
# a_zip = [1, 3, 5, 2, 4, 6]
# print(list(a_zip))
# Output should be [(1,2),(3,4),(5,6)]



tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys   = tweet.keys()     # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items  = tweet.items()

print(tweet_keys)
print(tweet_values)
print(tweet_items)

