import numpy as np

x = np.zeros((1,10,2),int)
print("Zeros:",x)

y = np.ones((1,20,2),int)
print("ones :",y)

a = np.arange(1,10)
b = np.arange(11,20)
print("Addition:", np.add(a,b))
print("subtract:", np.subtract(a,b))
print("divide:", np.divide(a,b))
print("multiply:", np.multiply(a,b))