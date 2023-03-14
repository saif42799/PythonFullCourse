# sets ---------------------------------------------

# empty set cannot look like this: empty_set = {} <- this would be a dictionary
#empty set
s = set()

f = {3,4,5,6,7,8,8}  # <- this is a set not a dict
print(type(f))

s.add(1)
s.add(2)
s.add(3)

print(s)  # print in {}, {1, 2, 3}

length = len(s)
print(length)

y = 4 in s
print(y)

print("------")
# sets are faster than lists
# 1st: Use "in" on a set and it is faster than using on a list
# 2nd: You can find distinct item in collections

#ex
item_list = [1,2,3,1,2,3]
print(item_list)

print(len(item_list))

set_list = set(item_list)
print(set_list)
print(len(set_list))

back_to_list = list(set_list)
print(back_to_list)
