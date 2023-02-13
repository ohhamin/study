import sys
input = sys.stdin.readline

def update(idx, w):
    while idx < n+m:
        tree[idx] += w
        idx += idx & -idx

def query(idx):
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= idx & -idx
    return res

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dvd = [0] * m + [1] * n
    dvd_idx = [0] + [i+m for i in range(n)]
    top_idx = m-1
    tree = [0] * (n+m)
    result = []
    for i in range(m, m+n):
        update(i, 1)
    for i in array:
        update(dvd_idx[i], -1)
        result.append(query(dvd_idx[i]))
        dvd_idx[i] = top_idx
        if top_idx:
            top_idx -= 1
            update(dvd_idx[i], 1)
    print(*result)
