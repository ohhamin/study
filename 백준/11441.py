import sys
input = sys.stdin.readline

def update(x, w):
    global n
    while x <= n:
        tree[x] += w
        x += x & -x
    
def query(x):
    tmp_result = 0
    while x > 0:
        tmp_result += tree[x]
        x -= x & -x
    return tmp_result

n = int(input())
array = [0] + list(map(int, input().split()))
tree = [0] * (n + 1)
for i in range(1, n+1):
    update(i, array[i])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(query(b) - query(a-1))