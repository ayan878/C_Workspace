#linear Search
def linearSearch(arr, target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1

#Binary Search
def binarySearch(arr,target):
    low =0
    high=len(arr)-1

    while mid<=target:
        mid=(low+high)//2
        if arr[mid]==target:
          return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[0,1,2,3,4,5,6,7,8,9]
target=4 
linear_index=linearSearch(arr,target)
binary_index= linearSearch(arr,target)

if linear_index !=-1:
     print("Linear search: Element",target, "found at index",linear_index)
else:
      print("Linear search: Element",target, "not found")  

if binary_index !=-1:
     print("Linear search: Element",target, "found at index",binary_index)
else:
      print("Linear search: Element",target, "not found")



import numpy as np
import os

x=np.arange(10,60)
print(x)

file=open("Create.txt",'w')
file.write("Create file successfully")
file.close()
file=open("Create.txt",'r')
data=file.read()
print(data)
file.close()
os.remove("Create.txt")

x=np.array([1,2,3,4,5])
print(x)
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y)

z=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(z)

# Create a 1D array filled with zeros
arr1 = np.zeros(5)
print(arr1)
# Create a 2D array filled with zeros
arr2 = np.zeros((3, 4))
print(arr2)
# Create a 3D array filled with zeros
arr3 = np.zeros((2, 3, 4))
print(arr3)