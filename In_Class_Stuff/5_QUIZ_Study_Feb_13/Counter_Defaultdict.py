# defaultdict ----------------------------------------------------------------------------------------------------------
from collections import defaultdict
import document as document

# Every one of these is slightly unwieldy, which is why defaultdict is useful.
# A defaultdict is like a regular dictionary, except that when you try to look
# up a key it doesn’t contain, it first adds a value for it using a zero-argument
# function you provided when you created it. In order to use defaultdicts,
# you have to import them from collections:


word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1


dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # {"Joel" : {"City": Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0, 1]}


# Counters -------------------------------------------------------------------------------------------------------------
from collections import Counter

# A Counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts:

c = Counter([0, 1, 2, 0])          # c is (basically) {0: 2, 1: 1, 2: 1}

# simple way to count from list
# recall, document is a list of words
word_counts = Counter(document)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)


