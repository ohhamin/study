import sys, heapq
input = sys.stdin.readline

n = int(input())
array = [[] for _ in range(3)]
for i in range(n):
    x, y, z = map(int, input().split())
    array[0].append((x, i))
    array[1].append((y, i))
    array[2].append((z, i))

array[0].sort()
array[1].sort()
array[2].sort()
edges = [[] for _ in range(n)]

for i in range(3):
    for j in range(1, n):
        tmp1 = array[i][j-1]
        tmp2 = array[i][j]
        edges[tmp1[1]].append((abs(tmp1[0] - tmp2[0]), tmp2[1]))
        edges[tmp2[1]].append((abs(tmp1[0] - tmp2[0]), tmp1[1]))

visited = [0] * n
queue = edges[0]
visited[0] = 1
count = 1
result = 0
heapq.heapify(queue)
while count < n:
    dist, nxt = heapq.heappop(queue)
    if visited[nxt] == 0:
        count += 1
        visited[nxt] = 1
        result += dist
        for i in edges[nxt]:
            if visited[i[1]] == 0:
                heapq.heappush(queue, i)
print(result)