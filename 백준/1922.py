import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
array = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    array[a].append((c, b))
    array[b].append((c, a))
visited[1] = 1
count = 1
result = 0
heap = array[1]
heapq.heapify(heap)
while count < n:
    val, nxt = heapq.heappop(heap)
    if visited[nxt] == 0:
        count += 1
        visited[nxt] = 1
        result += val
        for i in array[nxt]:
            if visited[i[1]] == 0:
                heapq.heappush(heap, i)

print(result)