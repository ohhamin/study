import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
tree = [1] * (n*4)

def init(s, e, idx):
    if s == e:
        tree[idx] = array[s]
        return tree[idx]
    mid = (s + e) // 2
    tree[idx] = init(s, mid, idx * 2) * init(mid + 1, e, idx * 2 + 1) % 1000000007
    return tree[idx]

def query(s, e, idx, l, r):
    if l > e or r < s:
        return 1
    if l <= s and r >= e:
        return tree[idx]
    mid = (s + e) // 2
    return query(s, mid, idx * 2, l, r) * query(mid + 1, e, idx * 2 + 1, l, r) % 1000000007

def update(s, e, idx, node, val):
    if node < s or node > e:
        return
    if s == e:
        tree[idx] = val
        return
    mid = (s + e) // 2
    update(s, mid, idx * 2, node, val)
    update(mid + 1, e, idx * 2 + 1, node, val)
    tree[idx] = tree[idx*2] * tree[idx*2 + 1] % 1000000007

init(0, n-1, 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)
    else:
        print(query(0, n-1, 1, b-1, c-1))