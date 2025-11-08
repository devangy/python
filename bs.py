




# bubblesort



def bs(array):
    # looping over the elements from start

    n = len(array)

    for i in range(n):
        # second pointer at 2 elements
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j], array[j+1]
                
    return array







array = [5,12,33,40,55,20,42,89]

print(bs(array))
