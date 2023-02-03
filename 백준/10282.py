import sys
import heapq
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    times = [10000001] * (n + 1)
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    queue = []
    times[c] = 0
    heapq.heappush(queue, (0, c))
    
    while queue:
        time, node = heapq.heappop(queue)
        if times[node] < time:
            continue
        for i in graph[node]:
            sum_time = i[0] + times[node]
            if sum_time < times[i[1]]:
                times[i[1]] = sum_time
                heapq.heappush(queue, (sum_time, i[1]))
    
    result_sum = 0
    result_time = 0
    for i in times:
        if i != 10000001:
            result_sum += 1
            result_time = max(result_time, i)
    print(result_sum, result_time)