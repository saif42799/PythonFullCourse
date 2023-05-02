# Chapter 5 ---------------------------------

# Series for 1-D data
# DataFrame for 2-D data
# Indexing
# Filtering
import pandas as pd

# Series for 1-D data
obj = pd.Series([4, 7, -5, 3])
print(obj)
print()

# indexing
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
# prints indexes out
print(obj2.index)
print()

# DataFrame for 2-D data
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print()

# specify order of data
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))
print()

# filtering
mask = obj2.isin([7, 3])
print(mask)










