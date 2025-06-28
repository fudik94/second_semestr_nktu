def type_check(type1, type2):  # decerator take two types
    def decorator(func):
        def wrapper(arg1, arg2):  # function take two arguments
            if type(arg1) != type1:  # checking first type
                raise TypeError(f"Argument 1 must be of type {type1}, got {type(arg1)}")
            if type(arg2) != type2:  # checking second type
                raise TypeError(f"Argument 2 must be of type {type2}, got {type(arg2)}")
            return func(arg1, arg2)  # if everything ok we call...
        return wrapper
    return decorator


@type_check(int, int)
def add(x, y):
    return x + y


@type_check(str, int)
def repeat_word(word, times):
    return word * times


# some testing
print(add(3, 5))  
try:
    print(add(3, "hello"))  
except TypeError as e:
    print(e)

print(repeat_word("Hi", 3))  
try:
    print(repeat_word(5, "Hello"))  
except TypeError as e:
    print(e)
