# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# a = outer_function('ajay')
# b = outer_function('abhay')
# a()
# b()



# def decorator_function(original_function):
#     def wrapper_function():
#         print('Executing...!')
#         original_function()
#         print('Executed...!')
#     return wrapper_function

# @decorator_function
# def display_function():
#     print('I love Nepal')

# display_function()


# Python Decorator allows to change the the behavior of a function without modifying the function itself.
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Start....!')
        original_function(*args, **kwargs)
        print('Finish...!')
    return wrapper_function

@decorator_function
def first_function():
    print('Hello')

@decorator_function
def second_function(name, address):
    print(f'He is {name}. lives in {address}')

first_function()
second_function('Ajay', 'ktm')



