class SkippingIterator:
    def __init__(self, obj, n=1):
        self.obj = obj  
        self.n = n  # step
        self.index = 0  # we start first element

    def __iter__(self):
        return self  

    def __next__(self):
        if self.index >= len(self.obj):
            raise StopIteration
        
        value = self.obj[self.index]  
        self.index += self.n  # skip  n  element
        return value  

# some testing
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1_iter = SkippingIterator(list1, 2)
print(list(list1_iter))  

str1 = "abcdefghi"
str1_iter = SkippingIterator(str1, 2)
print("".join(str1_iter))  
