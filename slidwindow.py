## sliding window implementation





def maxsum_subarray(arr,k):
    # computing the sum for the first window
    window_sum = sum(arr[:k])
    # temporary max sum of the window we have seen so far
    # we init with default window_sum 
    max_sum = window_sum
    
   # now we start sliding our window across the array
    # we sliding from end of our window index
    for i in range(k, len(arr)):
    # remove first element and add the element coming in window
    # arr[i] is index 3 why cuz we start from our window
    # end which is k = 3
    # window_sum + arr[i] (next value add in our window)
    # then minus the first elenment arr[i-k] = 3-3 = arr[0]
        window_sum += arr[i] - arr[i - k]
    # we are finding the max sub arr
    # comparing it our prev windows and returning that
        max_sum = max(window_sum, max_sum)

    return max_sum

arr = [2,1,5,1,3,2]
k = 3

print(maxsum_subarray(arr,k))
