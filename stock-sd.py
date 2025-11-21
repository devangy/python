



## buy sell stock slding window 
# in window calculate max profit 


def stock_sd(prices):

    n = len(prices)
    max_profit = 0
    
    # buy day will be 0 and sell will  
    for left in range(n):
        # expand right window based on condition
        right = left + 1
        while right < n:
            temp_profit = prices[right] - prices[left]
            max_profit = max(temp_profit,max_profit)
            right+= 1
    return max_profit



prices = [10,1,5,6,7,1]

print(stock_sd(prices))
