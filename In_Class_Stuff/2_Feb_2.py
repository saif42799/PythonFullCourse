# list comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]  # returns x [x  (for loop) (if statement)]
print(even_numbers)

squares = [x * x for x in range(5)]
print(squares)
even_squares = [x * x for x in even_numbers]
print(even_squares)


# dictionary and set = {}
square_dict = {x: x * x for x in range(5)}
print(square_dict)
square_set = {x * x for x in [1, -1]}
print(square_set)


zeros = [0 for _ in even_numbers]
print(zeros)


pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0, 0), (0, 1)... (9, 8), (9, 9
print(pairs)


passing_pairs = [(x, y)
                 for x in range(10)
                 for y in range(x + 1, 10)]
print(passing_pairs)


print() #----------------------------------------


# zip and argument unpacking
# zip =

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
[pair for pair in zip(list1, list2)]

[pair[0] for pair in zip(list1, list2)]  #prints 'a', 'b', 'c'

[pair[1] for pair in zip(list1, list2)]  #prints 1, 2, 3


print() #----------------------------------------


pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
letters, numbers = zip(*pairs)
print(letters)
print(numbers)


print() #----------------------------------------


pairs2 = [('a', 1, '$'), ('b', 2, '#'), ('c', 3, '@'), ('d', 4, '*')]
letters, numbers, symbol = zip(*pairs2)
print(letters)
print(numbers)
print(symbol)


print() #----------------------------------------


# Type Annotation





