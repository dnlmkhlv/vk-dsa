n = 6

dp = []

for i in range(1, n + 1):
    tmp = []
    for j in range(i):
        tmp.append(1)
    dp.append(tmp)

for row in range (1, n):
    for col in range(1, row):
        dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]

print(dp)