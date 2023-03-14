# dictionary section ------------------------------------------

import document
#             Key     : Value
hero_dict = {"Batman" : 1, "Superman" : 2, "Wonder Woman" : 3}

hero_rank_num = hero_dict["Superman"]
print("Ranked number: ", hero_rank_num)

# KeyError
try:
    hero_nonExsit = hero_dict["Owl man"]
except KeyError:
    print("Wrong universe")

# in
hero_member = "Batman" in hero_dict
print(hero_member)

hero_nonMemebr = "Bum man" in hero_dict
print(hero_nonMemebr)

# get method
wonder_out = hero_dict.get("Wonder Woman", 0)
print(wonder_out)

cat_in = hero_dict.get("Catwoman", 0)
print(cat_in)

# replace and add
hero_dict["Wonder Woman"] = 4

hero_dict["Catwoman"] = 3

print(hero_dict)


# defaultdict - idk

stuff = {"AmericanPythoninta"}
word_counts = {}
for i in stuff:
    if i in word_counts:
        word_counts[i] += 1
    else:
        word_counts[i] = 1

print(word_counts)