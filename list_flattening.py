"""
List Flattening using recursion and other methods too.
input - [[1, 2, 3], [4]]
output - [1, 2, 3, 4]
"""
# Method 1: Recurrsion. Risk of recurrsion depth limit.
def flatten(seq):
  """ This can handle any arbitrary depth of nesting """
  for x in seq:
    if isinstance(x, (tuple, list)):
      yield from flatten(x)
    else:
      yield x

a = [[1, 2, 3], [4]]
b = list(flatten(a))

# Method 2: Library solution using itertools.chain.from_iterable ( Faster than any method for large inputs as its written in C )
from itertools import chain
b = list(chain.from_iterables(a))

# Method 3: Comprehension (Clean and Fast but you should know the level of nesting)
b = [item for sublist in a for item in sublist]

# Method 4: Star unpacking (When you already know the length)
b = [*a[0], *a[1]]
