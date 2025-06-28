

# we create a decorator named cache_results that
def cache_results(func):
    our_dictionary={}  #we use a dictionary to store previously computed results
    def wrapper(*args):
        # print if the result is already stored.
        
        if args in our_dictionary:  
            print("Cache hit for {args}: returning cached result")
            return our_dictionary[args]
        # print this if the function is executed.
        else:
            print("Calculating result for {args}")

            result=func(*args)  # call original function to calculate result

            our_dictionary[args] = result # save result in our dictionary

            return result
    return wrapper


# we make Fibonacci function test without decorator
def fibonacci(n):
    if n <=1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

print("RESULT WITHOUT DECERATOR :" , fibonacci(10))

# we make Fibonacci function test with decorator

@cache_results
def fibonacci(n):
    if n <=1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

print("RESULT WITH DECERATOR :" , fibonacci(10))



