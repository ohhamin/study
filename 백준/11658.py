import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
sums = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sums[i][j] = sums[i][j-1] + sums[i-1][j] + array[i][j] - sums[i-1][j-1]
for _ in range(m):
    cal = list(map(int, input().split()))
    if cal[0] == 0:
        tmp_num = cal[3] - array[cal[1]][cal[2]]
        for i in range(cal[1], n+1):
            for j in range(cal[2], n+1):
                sums[i][j] += tmp_num
    else:
        print(sums[cal[3]][cal[4]] - sums[cal[3]][cal[2]-1] - sums[cal[1]-1][cal[4]] + sums[cal[1]-1][cal[2]-1])