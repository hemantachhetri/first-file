prices = [7, 1, 5, 3, 6, 4]
left = 0
right = 1
max_profit = 0

while right < len(prices):
    current_profit = prices[right] - prices[left]
    print ('current_profit', current_profit)
    if current_profit > 0:
        if max_profit < current_profit:
            max_profit = current_profit
            right = right + 1
    else:
        left = left + 1
        right = right + 1
        