import sys
input = sys.stdin.readline

def binary_search(x):
    s = 0
    e = n
    while s <= e:
        mid = (s + e) // 2
        if ordered_array[mid] == x:
            return mid
        elif ordered_array[mid] > x:
            s = mid+1
        else:
            e = mid
    return e

def update(idx):
    while idx < n+1:
        tree[idx] += 1
        idx += idx & -idx

def query(idx):
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= idx & -idx
    return res

n = int(input())
array = [10000000001] + [int(input()) for _ in range(n)]
ordered_array = sorted(array, reverse=True)
tree = [0] * (n + 1)
for i in array[1:]:
    idx = binary_search(i)
    update(idx)
    print(query(idx))