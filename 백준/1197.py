import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v)]
visited = [0] * v

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append((c, a-1, b-1))
    graph[b - 1].append((c, b-1, a-1))

visited[0] = 1
result = 0
count = 1
queue = graph[0]
heapq.heapify(queue)

while count < v:
    dist, now, desti = heapq.heappop(queue)
    if visited[desti] == 0:
        visited[desti] = 1
        result += dist
        for i in graph[desti]:
            if not visited[i[2]]:
                heapq.heappush(queue, i)
        count += 1

print(result)