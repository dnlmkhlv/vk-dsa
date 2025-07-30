def getRow(rowIndex):
    n = rowIndex + 1
    dp = []

    for i in range(n):
        tmp = [1] * (i + 1)
        for j in range(1, i):
            tmp[j] = dp[i - 1][j - 1] + dp[i - 1][j]
        dp.append(tmp)

    return dp[rowIndex]

print(getRow(5))