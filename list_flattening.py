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

# Method 2: Library solution using itertools.chain.from_iterable ( Faster than any method for large inputs having single level nesting as its written in C )
from itertools import chain
b = list(chain.from_iterables(a))

# Method 3: Comprehension (Clean and Fast but good for small inputs and single level nesting)
b = [item for sublist in a for item in sublist]

# Method 4: Star unpacking (When you already know the length)
b = [*a[0], *a[1]]

# Method 5:  Iterative stack for deep nesting (No recurrsion and Eliminates python recurrsion depth ceiling)
from collections import deque
from collections.abc import Iterable

_ATOMIC = (str, bytes, bytearray) # Just to ignore these as iterables in if condition

def deep_flatten(seq):
  stack = deque([iter(seq)]) # start with top iterator
  while stack:
    try:
      item = next(stack[-1]) # look at the current iterator
    except StopIteration:  
      stack.pop()            # Exhausted pop it
      continue

    if isinstance(item, Iterable) and not isinstance(item, _ATOMIC):
      stack.append(iter(item))
    else:
      yield item

b = list(deep_flatten(a))
