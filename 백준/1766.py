import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0, []] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b][0] += 1
    graph[a][1].append(b)

result = []
question = []
for i in range(1, n + 1):
    if graph[i][0] == 0:
        heapq.heappush(question, i)

while question:
    solve = heapq.heappop(question)
    result.append(solve)
    for i in graph[solve][1]:
        graph[i][0] -= 1
        if graph[i][0] == 0:
            heapq.heappush(question, i)

print(*result)