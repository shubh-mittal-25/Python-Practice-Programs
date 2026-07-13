# Python Decorator
import time

def delay_decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator_function
def say_hello():
    print("Hello")
@delay_decorator_function
def say_bye():
    print("Bye")
@delay_decorator_function
def say_goodbye():
    print("Goodbye")

say_hello()
say_bye()
say_goodbye()