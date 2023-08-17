 
def bubble_sort(array):  
   
    for i in range(len(array)):  
        for j in range(0,len(array)-1-i):  
            if(array[j]>array[j+1]):  
                temp = array[j]  
                array[j] = array[j+1]  
                array[j+1] = temp   
  
data = [5, 3, 8, 6, 7, 2]  
print("Data before sorted: ", data)  

print("The sorted in ascending order: ", data)  

