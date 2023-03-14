# zip
# Often we will need to zip two or more iterables together.
# The zip function transforms multiple iterables into a single
# iterable of tuples of corresponding function:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]

# unzip a list
pairs = [('a', 1), ('b', 2), ('c', 3)]

letters, numbers = zip(*pairs)
# same as
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

a_zip = (1, 3, 5) (2, 4, 6)
print(list(a_zip))
[(1,2),(3,4),(5,6)]


