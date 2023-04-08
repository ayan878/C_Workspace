import numpy as np

y=[1,2,3,4]
x=np.array([1,2,3,4])
D=np.array([[1,2,3,4]])
_2D=np.array([[1,2,3,4],[5,6,7,8]])
_3D=np.array([[[1,2,3,],[4,5,6],[7,8,9]]])
print(x)
print(type(D)) #array
print(type(y)) #list
print(_2D[1][1]) #6
print(_3D[0][0][0]) #1

# The function is used to generate value 0-1
var =np.random.rand(4)
print(var)

# The function is used to generate close to zero it may return positive and negaive as well
var =np.random.randn(4)
print(var)

print('Multidimentioanl Array')
var =np.random.randn(2,5) # Multidimentional array
print(var)


print('Random Integer')
var = np.random.randint(2,7,5) # randint( min, max, total value)
print(var)