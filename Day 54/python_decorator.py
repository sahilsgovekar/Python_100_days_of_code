import time

def decorator(function):
    def inner_function():
        time.sleep(2)
        function()  
        function()
    return inner_function

@decorator
def hello():
    print("Hello World")

# test = decorator(hello)
# test()

hello()