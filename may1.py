


arr = [8,5,8,2,6,2,5]

k= 3


def slid_win(arr,k):

    if len(arr) < k:
        return 0


    window_sum = sum(arr[:k])
    max_sum = window_sum


    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum
            
print(slid_win(arr,k))

