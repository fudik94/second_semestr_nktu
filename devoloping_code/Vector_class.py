class Vector:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        
        return Vector(self.x + other.x , self.y + other.y)
    
    def __mul__(self,scalar):

        return Vector(self.x + scalar , self.y + scalar)

    def __str__(self):
        return(f"{self.x , self.y }")
    
# Creating vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

#Adding vectors
v3 = v1 + v2
print(v3)


#Another example
v4 = Vector(-1, 7) + Vector(3, -2)
print(v4)

#Scolar vectors
v5 = v1 * 2
print(v5)




        
