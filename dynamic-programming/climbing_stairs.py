dp = [1, 1]
def jump(n):
    for _ in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

print(jump(3))
print(jump(8))