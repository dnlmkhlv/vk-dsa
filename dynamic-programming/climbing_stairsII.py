dp = [1, 1, 2]

def jump(n):
    while len(dp) <= n:
        dp.append(dp[-1] + dp[-2] + dp[-3])
    return dp[n]
