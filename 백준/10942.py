import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n - i):
        k = i + j
        if k == j:
            dp[j][k] = 1
        elif array[j] == array[k]:
            if i == 1:
                dp[j][k] = 1
            elif dp[j + 1][k - 1] == 1:
                dp[j][k] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])