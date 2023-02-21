# set = collection which is unordered, unindexed. No duplicate values
# faster than list
# used {}

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup",  "knife"}
utensils.add("napkin")
utensils.remove("fork")

utensils.update(dishes)

dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)

print()

for x in dinner_table:
    print(x)

print()

print(utensils.difference(dishes))

print()

print(utensils.intersection(dishes))