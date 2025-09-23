

"""
first run a outer loop from start  to the end of array 
then for every i'th iteration run a inner loop to check the element
on the left side of the element if it is greater than the i element
swap them or else move on
"""

def selectionsort():
    n = len(array)

    for i in range (n):
        for j in range (i+1,n):
            if array[j] < array[i]:
                array[i] = array[j]




array = [2,1,21,4,33,5,99]
hello()
