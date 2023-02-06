import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [0 for _ in range(n * 4)]
array = []
for _ in range(n):
    array.append(int(input()))

def make_tree(node, left, right):
    if left == right:
        tree[node] = array[left]
        return tree[node]
    mid = left + (right - left) // 2
    l_node = make_tree(2*node, left, mid)
    r_node = make_tree(2*node+1, mid+1, right)
    tree[node] = min(l_node, r_node)
    return tree[node]

def find(s, e, node, left, right):
    if e < left or s > right:
        return 1000000001
    if e >= right and s <= left:
        return tree[node]
    mid = left + (right - left) // 2
    l_node = find(s, e, 2*node, left, mid)
    r_node = find(s, e, 2*node+1, mid+1, right)
    return min(l_node, r_node)

make_tree(1, 0, n-1)
for _ in range(m):
    a, b = map(int, input().split())
    result = find(a-1, b-1, 1, 0, n-1)
    print(result)