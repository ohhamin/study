import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()
        numbering[x][y] = z
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and array[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    counts.append(count)

n, m = map(int, input().split())
array = [list(map(int, input().strip())) for _ in range(n)]
numbering = [[0] * m for _ in range(n)]
counts = []
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
num = 1
for i in range(n):
    for j in range(m):
        if not array[i][j] and not visited[i][j]:
            bfs(i, j, num)
            num += 1
for i in range(n):
    tmp = ''
    for j in range(m):
        if array[i][j]:
            tmp_count = 1
            tmp_set = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and numbering[ni][nj]:
                    tmp_set.add(numbering[ni][nj] - 1)
            for tmp_num in tmp_set:
                tmp_count += counts[tmp_num]
            tmp_count %= 10
            tmp += str(tmp_count)
        else:
            tmp += '0'
    print(tmp)