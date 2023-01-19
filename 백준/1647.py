import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x_p = find_parent(x)
    y_p = find_parent(y)
    if x_p > y_p:
        parent[x_p] = y_p
    else:
        parent[y_p] = x_p

n, m = map(int, input().split())
road = []
result = 0
end = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    road.append([c, a, b])

parent = list(range(n + 1))
road.sort()

for item in road:
    if find_parent(item[1]) != find_parent(item[2]):
        union(item[1], item[2])
        result += item[0]
        end = item[0]

print(result - end)