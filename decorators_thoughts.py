import time

def timer(func):
  """ Calculating the time taken by a function to run """
  def wrapper(*args, **kwargs):
    """ wrapper function to call the original function
        It can be named anything.
        *args and **kwargs are just to handle any parameters used in original function
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Time taken to run the function {func.__name__} is {end-start:.2f} second(s)")
    return result
  return wrapper

def logger(func):
  """ Add logging for function """
  def wrapper(*args, **kwargs):
    """ wrapper function to call the original function
        It can be named anything.
        *args and **kwargs are just to handle any parameters used in original function
    """
    print(f"[LOG] Calling {func.__name__}")
    result = func(*args, **kwargs)
    print(f"[LOG] Called {func.__name__}")
    return result
  return wrapper
    
@timer
def slow_function():
  """ I am a slow function """
  time.sleep(2)
  print("Done!")

@logger
def greet(name):
  """ Greet with Name """
  print(f"Hello, {name}!")

slow_function()
greet("TechieJ")
