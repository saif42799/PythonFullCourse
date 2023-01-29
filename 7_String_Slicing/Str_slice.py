#slicing = create a substring by extracting elements from another string
#        indexing[] or slice[]
#        [start:stop:step]

#indexing[]-------------------------------------------------------------
name = "Saif Shaikh"

first_letter = name[0]
first_name = name[0:4]
#or
or_first_name = name[:4]

last_name = name[5:11]
#or
or_last_name = name[5:]

#step
funky_name = name[0:11:2]
#or
or_funky_name = name[::2]

#reverse String
revered_name = name[::-1]

print(first_letter)
print(first_name)
print(or_first_name)
print(last_name)
print(or_last_name)
print(funky_name)
print(or_funky_name)
print(revered_name)
print("\n")

#slice[]----------------------------------------------------------------
website1 = "http://google.com"
website2 = "http://youtube.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
