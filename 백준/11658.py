import sys
input = sys.stdin.readline

def update(x, y, w):
    global n
    while y <= n:
        tmp_x = x
        while tmp_x <= n:
            tree[y][tmp_x] += w
            tmp_x += tmp_x & -tmp_x
        y += y & -y

def query(x, y):
    result = 0
    while y > 0:
        tmp_x = x
        while tmp_x > 0:
            result += tree[y][tmp_x]
            tmp_x -= tmp_x & -tmp_x
        y -= y & -y
    return result
        
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
tree = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        update(i+1, j+1, array[i][j])

for _ in range(m):
    cal = list(map(int, input().split()))
    if cal[0] == 0:
        update(cal[1], cal[2], cal[3] - array[cal[1]-1][cal[2]-1])
        array[cal[1]-1][cal[2]-1] = cal[3]
    else:
        print(query(cal[3], cal[4]) - query(cal[3], cal[2]-1) - query(cal[1]-1, cal[4]) + query(cal[1]-1, cal[2]-1))