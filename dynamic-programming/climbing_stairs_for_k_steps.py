def jump(n, k):
    dp = [1]  # base case: 1 way to reach step 0
    for i in range(1, n + 1):
        total = 0
        for j in range(1, min(k, i) + 1):
            total += dp[i - j]
        dp.append(total)
    return dp[n]


print(jump(3,2))