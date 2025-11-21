


def insort(array):
    n = len(array)
    for i in range(1,n ):
        # check the sorted part 
        insert_index = i
        current_value = array.pop(i)
        for j in range(i-1,-1, -1):
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value)
    return array
            





array =  [ 7, 12, 9, 11, 3]

print(insort(array))
