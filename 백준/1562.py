n = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(n + 1)]
dj = [-1, 1]

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(1 << 10):
            for a in range(2):
                nj = j + dj[a]
                if 0 <= nj < 10:
                    dp[i][j][(1 << j) | k] += dp[i-1][nj][k]
                dp[i][j][(1 << j) | k] %= 1000000000

result = 0
for i in range(1, 10):
    result += dp[n][i][(1 << 10) - 1]
    result %= 1000000000
print(result)