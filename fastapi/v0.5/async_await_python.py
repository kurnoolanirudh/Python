import time 

async def say_hello():
    print("I/O process start")
    time.sleep(2)
    print("I/O process end")
    return "I/O data"

# The key here is the await. It tells Python that it has to wait for say_hello() to finish doing its thing
# before storing the results in data. With that, Python will know that it can go and do something else in the meanwhile (like receiving another request).
# You might have noticed that await can only be used inside of functions defined with async def.
# But at the same time, functions defined with async def have to be "awaited". So, functions with async def can only be called inside of functions defined with async def too.
# So, about the egg and the chicken, how do you call the first async function?
#If you are working with FastAPI you don't have to worry about that, because that "first" function will be your path operation function, and FastAPI will know how to do the right thing.

async def print_date():
    data = await say_hello()
    print(data)
