 






# sliding window algo start from left ptr and right ptr\
# we start from a window left and right 


def sw(array):

    left = 0
    win_size = 2

    for i in range(len(array)):
        window = array[i : i + win_size]
        print(window)



array = [23,8,11,59,33,60,3,98]
       
sw(array)

