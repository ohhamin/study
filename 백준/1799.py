def back(r, c, count):
    global tmp_result
    if n % 2:
        if c == n:
            r += 1
            c = 0
        elif c == n + 1:
            r += 1
            c = 1
    else:
        if c == n:
            r += 1
            c = 1
        elif c == n + 1:
            r += 1
            c = 0
    if r == n:
        tmp_result = max(tmp_result, count)
        return
    if array[r][c] == 1 and visited[0][r + c] == 0 and visited[1][r - c] == 0:
        visited[0][r + c] = 1
        visited[1][r - c] = 1
        back(r, c+2, count+1)
        visited[0][r + c] = 0
        visited[1][r - c] = 0
    back(r, c+2, count)

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (n * 3) for _ in range(2)]
tmp_result = 0
result = 0
back(0, 0, 0)
result += tmp_result
tmp_result = 0
back(0, 1, 0)
print(result + tmp_result)