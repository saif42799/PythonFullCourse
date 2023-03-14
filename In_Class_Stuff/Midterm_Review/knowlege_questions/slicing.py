# Slicing --------------------------------------------

# slice with list
# [Start : Stop : End]
num_list = [1, 2, 3, 4, 5, 6]

start_list = num_list[2:]
print(start_list)

stop_list = num_list[:3]
print(stop_list)

stop_list2 = num_list[:-3]
print(stop_list2)

combo_list = num_list[0:5:2]
print(combo_list)

combo_list2 = num_list[::3]
print(combo_list2)

all_list = num_list[:]
print(all_list)
