n = int(input())
train = list(map(int, input().split()))
m = int(input())
sums = [0] * (n+1)
for i in range(1, n+1):
    sums[i] = sums[i-1] + train[i-1]
dp = [[0] * (n+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i*m, n+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], sums[j] - sums[j-m])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + sums[j] - sums[j-m])
print(dp[-1][-1])