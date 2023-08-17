

def insertionSort(array):
    for i in range(1,len(array)):
        temp=array[i]
        j=i-1

        while j>=0 and temp <array[j]:
              array[j+1]=array[j]
              j=j-1
        array[j+1]=temp
       
arr=[99,50,1,4,30,16]
n =len(arr)
print("Given array is:")
for i in range(n):
     print(arr[i],end=" ")
insertionSort(arr)
print('\n\nSorted Array in Ascending Order:')
print(arr)




