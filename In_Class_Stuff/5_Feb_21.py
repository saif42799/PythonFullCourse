# Object Oriented Programming

# OOP: Encapsulation and data abstraction


class Book:
    material = "paper"
    cover = "paperback"
    ail_books = []

Book.material = "metal"
print(Book.material)

my_book = Book()
print(my_book.material)

my_book.cover = "herdcover"
print(my_book.cover)


class River:
    # class attributes
    all_rivers = []

    # instance attributes
    # constructor
    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("The length of the {0} is {1} km ".format(self.name, self.length))

volga = River("Volga", 3530)
Blah = River("Undiscovered fart", 4409)
Nile = River("Nile", 3489)

print("River Name:", volga.name, "| River length:", volga.length)

print()

for river in River.all_rivers:
    print("River Name:", river.name, "| River length:", river.length)

volga.get_info()
River.get_info(volga)