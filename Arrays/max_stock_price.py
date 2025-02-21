def single_max_profit(prices):
    if not prices:
        return 0 
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price                     
        if profit > max_profit:
            max_profit = profit
    return max_profit

def multiple_max_profit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0, n):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit 
            
prices =[100,134,56,45,2,100]
print(single_max_profit(prices))

prices = [100, 134, 56, 45, 2, 100, 150, 120]
print(multiple_max_profit(prices))            