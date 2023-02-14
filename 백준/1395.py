import sys
input = sys.stdin.readline

def update(idx, w):
    while idx < n+1:
        tree[idx] += w
        idx += idx & -idx

def query(idx):
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= idx & -idx
    return res

n, m = map(int, input().split())
tree = [0] * (n+1)
switch = [[-1, 0] for _ in range(n+1)]
for _ in range(m):
    o, s, t = map(int, input().split())
    if o == 0:
        for i in range(s, t+1):
            if switch[i][0] == -1:
                switch[i][0] = 1
            else:
                switch[i][0] = -1
            if switch[i][1] == 0:
                switch[i][1] = 1
            else:
                switch[i][1] = 0
    else:
        for i in range(s, t+1):
            if switch[i][1] == 1:
                update(i, switch[i][0])
                switch[i][1] = 0
        print(query(t) - query(s-1))