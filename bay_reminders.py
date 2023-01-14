# Debug with this line
import code; code.interact(local=locals())


# Use SETs "var = set()" instead of LISTS "var = []" when you dont care about order 
# but do care about uniqueness and set logic (&, ||..)
a = set(['a', 'b', 'c'])
a = {'a', 'b', 'c'}
a.add('d')
a.remove('e') # raises error
a.discard('e') # silent fails
overlap = a & b

# a LIST can act as a queue easily by using
mylist.pop()  # last index
mylist.pop(0)
mylist.append(x)  # last index
mylist.insert(0, x)
mylist.extend(['a', 'b', 'c']) # adds the elements, not a nested list

# Use tuples for coordinates
# they are immutable so can be put in sets! (for uniqueness, set logic, etc)
coord = (x, y)

# Cast back and forth between types
"".join(a)   # don't use string(a)
list(a)
int(a)

# Use dictionaries to map input characters directly to more complex strings or tuples
deltas = { 'U' = (-1,0), 'D' = (1,0), 'R' = (0, 1), 'L' = (0,-1) }

# Array indexing
myarr[5:]  #index 5 to end
myarr[0:5] #index 0 up to not including index 5

# Ranges
for i in range (5)
for i in range (0, 5, 1)

# Group array into chunks
groups = [raw[i:i+3] for i in range(0, len(raw), 3)]

# Zip two arrays together, as a list of tuples
new = list(zip( a, b ))

# Use eval to execute code in a string, and return the output
# Execute doesn't return the output, and requires global var passing
var = eval("5 + 10")
exec("var = 5 + 10") # you'll have var scope issues

# Custom sort functions
from functools import cmp_to_key
output = sorted(input, key=cmp_to_key(compare), reverse=True) 
def compare(l, r):
  # return 1, 0, -1  
  

# File Loading
with open('input_bay.txt', 'r') as file:
  # BASIC
  # returns a list of strs, with \n char at the end of each str
  input = file.readlines()

  # BEST
  # returns a single massive string, and then runs str.splitlines() on it
  # this also gets rid of \n characters at end
  input = file.read().splitlines()

  # EQUIVALENT ALT
  # returns a list of strs, with trailing spaces or \n's deleted
  # can use '.strip()' to apply to both sides
  input = [line.rstrip() for line in file.readlines()]

  # COMPLEX 
  # instead of one-top level list with all strings inside it,
  # have two layers of lists where the inner layer breaks up the input by double line break
  input = file.read()
  input = input.split("\n\n")
  input = list( map(lambda s: s.split("\n"), input) ) 
