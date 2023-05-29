
#linear Search
def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
    return -1

#binary search
def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    while low <= high:
        mid=low+high//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
        
    return -1
arr=[1,2,3,4,5,6,7,8,9]
target=4

linear_index= linearSearch(arr,target)
if linear_index !=-1:
    print("Linear search:Element",target,"at index",linear_index)
else:
    print("Linear search:Element",target,"not found")

binary_index= linearSearch(arr,target)
if linear_index !=-1:
    print("Linear search:Element",target,"at index",binary_index)
else:
    print("Linear search:Element",target,"not found")
