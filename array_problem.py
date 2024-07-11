# remove odd numbers from a given array without using another array.
array=[1,2,3,4,5,6,7,8,9,10]

for i in range(9,-1,-1):   
    if (array[i])%2==0:
        pass
    else:
        array.remove(array[i])
        
print(array)
