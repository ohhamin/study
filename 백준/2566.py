import sys
input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(9)]

result = 0
resultIndex = [0, 0]
for i in range(9):
    for j in range(9):
        if graph[i][j] >= result:
            result = graph[i][j]
            resultIndex[0] = i + 1
            resultIndex[1] = j + 1

print(result)
print(*resultIndex)