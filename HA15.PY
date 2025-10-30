def cut_rod(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)

    for length in range(1, n + 1):
        max_val = -float("inf")
        for cut in range(1, length + 1):
            if cut <= len(prices):
                value = prices[cut - 1] + dp[length - cut]
                if value > max_val:
                    max_val = value
                    cuts[length] = cut
        dp[length] = max_val  
    
    res = []
    length = n
    while length > 0:
        res.append(cuts[length])
        length -= cuts[length]

    return dp[n], res


prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
max_profit, cuts = cut_rod(prices, n)
print("Maximum value:", max_profit)
print("Recommended lengths:", cuts)