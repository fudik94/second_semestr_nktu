def pascals_triangle():
    row = [1]  # we start from first str [1]
    while True:
        yield row  # we give current str
        new_row = [1]  
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])  # sum neigber str
        new_row.append(1)  # last str in new 
        row = new_row  # go to new str

# sample
gen = pascals_triangle()
for _ in range(5):
    print(next(gen))

