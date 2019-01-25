def buy_sell_stocks(arr):
    if arr is None or len(arr) < 2:
        return None

    cur_buy = arr[0]
    global_sell = arr[1]
    global_profit = global_sell - cur_buy

    cur_profit = float('-inf')
    arr_l = len(arr)

    for i in range(1, arr_l):
        cur_profit = arr[i] - cur_buy
        
        if cur_profit > global_profit:
            global_profit = cur_profit
            global_sell = arr[i]

        if cur_buy > arr[i]:
            cur_buy = arr[i]

    return global_sell - global_profit, global_sell


array = [1, 2, 3, 4, 3, 2, 1, 2, 5]
result = buy_sell_stocks(array)
print ("Buy Price : " + str(result[0]) + " Sell Price: " + str(result[1]))

array = [8, 6, 5, 4, 3, 2, 1]
result = buy_sell_stocks(array)
print("Buy Price : " + str(result[0]) + " Sell Price: " + str(result[1]))
