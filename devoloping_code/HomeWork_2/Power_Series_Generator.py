

def power_series(x):
    power = 0 #this is first power ,start postion
    while True: #infinite loop
        yield x** power# each x make power 
        power +=1 #after each result we add 1 power


gen1 = power_series(2)
print([next(gen1) for _ in range(5)])

gen2 = power_series(3)
print([next(gen2) for _ in range(4)])  
   
    