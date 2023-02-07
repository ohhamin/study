n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(n + 1)]

result = 100000001
for i in range(1, n + 1):
    for j in range(1, sum(cost) + 1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i-1][j], memory[i] + dp[i-1][j - cost[i]])
            if dp[i][j] >= m:
                result = min(result, j)
        else:
            dp[i][j] = dp[i-1][j]
print(result)