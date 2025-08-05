dp = [1, 1]

def jump(n):
    while len(dp) <= n:
        dp.append(dp[-1] + dp[-2])
    return dp[n]

print(jump(8))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
