import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0, 1))
    visited[0][x][y] = 1
    while queue:
        x, y, z, dist = queue.popleft()
        if x == n-1 and y == m-1:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 1 and z < k and visited[z + 1][nx][ny] == 0:
                    queue.append((nx, ny, z + 1, dist + 1))
                    visited[z + 1][nx][ny] = 1
                elif array[nx][ny] == 0 and visited[z][nx][ny] == 0:
                    queue.append((nx, ny, z, dist + 1))
                    visited[z][nx][ny] = 1
    return -1

n, m, k = map(int, input().split())
array = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * (m) for _ in range(n)] for _ in range(k + 1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
print(bfs(0, 0))