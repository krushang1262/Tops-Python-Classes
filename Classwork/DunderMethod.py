class Calc:
    
    def __init__(self, x):
        self.x = x
        
    def __add__(self, other):
        return self.x + other.x
    
    def __mul__(self, other):
        return self.x * other.x
    
    def __div__(self, other):
        return self.x / other.x

c1 = Calc(5)
c2 = Calc(5)
print(c1.__add__(c2))
print(c1.__mul__(c2))
print(c1.__div__(c2))