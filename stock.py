




def stock(prices: list[int]):
    # for each day in prices iterate over all the other days to 
    # calculate max profit and compare with temp_total
    # bruteforce method
    n = len(prices)
    max_profit = 0


    for i in range(n):
        for j in range(1,n):
            temp_total = prices[j] - prices[i]
            if temp_total > max_profit:
                max_profit = temp_total
                j += 1
    return max_profit





    

# price of stock on i th day
prices = [10,1,5,6,7,1]

print(stock(prices))

