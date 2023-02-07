import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    dp[x][0] += 1
    for i in tree[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += min(dp[i][0], dp[i][1])
            dp[x][1] += dp[i][0]

n = int(input())
tree = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
print(min(dp[1]))