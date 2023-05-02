from collections import Counter

# counts words, letters, numbers
#Counter
word_count = "the waves hit the shore".split(" ")
print(Counter(word_count))

#Sets
primes_below_10 = {2,3,5,7,2,3,5,7}
s = set()
s.add(1)
s.add(2)
s.add(3)

setstuff = set(primes_below_10)
print(setstuff)

#all
#any

#sorting
x = [4,1,2,3]
t = [4,1,2,3]
y = sorted(x)
print(y)

t.sort()
print(t)

