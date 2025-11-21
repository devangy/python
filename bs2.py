






def bs2(array):
    # first element is already sorted
    for i in range(len(array)):
        # starting from second element 
        for j in range(len(array)):
            #check with previous element if less than this swap
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

    return array
    






array = [11,75,15,26,62,59,0]


print(bs2(array))
