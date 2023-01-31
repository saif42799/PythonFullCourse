# lists = used to store multiple items in a single variables

food = ["pizza", "hamburgers", "hotdogs", "spaghetti"]

food[0] = "sushi" # replaces element at index 0

print(food)  # prints whole list
print(food[1])  # prints element in list

print()

#display all elements in list
for i in food:
    print(i)

print()
#list functios
food.append("ice Cream")  # adds element to list
food.remove("hotdogs")
food.pop()  # removes last elements
food.insert(0, "cake")  # adds element to given index
food.sort()
food.clear()  # clears list

print(food)
