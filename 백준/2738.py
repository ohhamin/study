n, m = map(int, input().split())
array1 = [list(map(int, input().split())) for _ in range(n)]
array2 = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        result[i][j] = array1[i][j] + array2[i][j]
for i in range(n):
    print(*result[i])