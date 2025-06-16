import time

def timer(func):
""" Calculating the time taken by a function to run """
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Time taken to run the function {func.__name__} is {end-start:.2f}")
    return result
  return wrapper

@timer
def slow_function():
  time.sleep(2)
  print("Done!")

slow_function()
