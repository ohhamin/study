import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
result = 0

gem = []
for i in range(n):
    j = list(map(int, input().split()))
    heapq.heappush(gem, j)

pack = []
for i in range(k):
    p = int(input())
    heapq.heappush(pack, p)

tmp = []
while pack:
    c = heapq.heappop(pack)
    while gem and c >= gem[0][0]:
        heapq.heappush(tmp, -heapq.heappop(gem)[1])
    if tmp:
        result -= heapq.heappop(tmp)
    elif gem == []:
        break
print(result)
