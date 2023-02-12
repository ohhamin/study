import sys, heapq
input = sys.stdin.readline

while 1:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    array = [[] for _ in range(m)]
    visited = [0] * m
    result = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        array[x].append((z, y))
        array[y].append((z, x))
        result += z
    queue = array[0]
    heapq.heapify(queue)
    visited[0] = 1
    count = 1
    while count < m:
        val, nxt = heapq.heappop(queue)
        if visited[nxt] == 0:
            result -= val
            count += 1
            visited[nxt] = 1
            for i in array[nxt]:
                if visited[i[1]] == 0:
                    heapq.heappush(queue, i)
    print(result)