

"""
 first we will place a ptr at i = 0  this is outer 
 now we will place the second ptr at j = 1 then we 
 will check in every i'th iteration go through all the other elements
 outer will run from 0 to lengh of array
 inner will run from 1 to i-1
 if we find i == j we will increment j + 1
 duplicate found
 else we will swap the front of the current element i with j
 i + 1 = j

"""





def duplicate():
    n = len(arr)
    for i in range n: 
        for j in range n-1:
            if arr[i] == arr[j]:
               j +=1 
            else:
                arr[i+1] = arr[j]
                i += 1
                j += 1





duplicate(arr)

arr = [1,1,2,2,3,3,4,4]



