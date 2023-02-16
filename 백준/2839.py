n = int(input())
dp = [-1 for _ in range(n)]
if n >= 5:
    dp[2] = 1
    dp[4] = 1
    for i in range(5, n):
        a = 5000
        b = 5000
        if dp[i-3] != -1: a = dp[i-3] + 1
        if dp[i-5] != -1: b = dp[i-5] + 1
        if a != 5000 or b != 5000: dp[i] = min(a, b)
    print(dp[-1])
else:
    dp[2] = 1
    print(dp[-1])
