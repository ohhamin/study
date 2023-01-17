import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
singers = [[set(), set()] for _ in range(n + 1)]

for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, len(order)):
        singers[order[i]][0].update(order[1:i])
        singers[order[i]][1].update(order[i+1:])

queue = deque()
result = []
for i in range(1, n + 1):
    if not singers[i][0]:
        queue.append(i)

while queue:
    result.append(queue.popleft())
    for i in singers[result[-1]][1]:
        singers[i][0].remove(result[-1])
        if not singers[i][0]:
            queue.append(i)
if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)