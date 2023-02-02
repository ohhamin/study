n = int(input())
k = int(input())
array = list(map(int, input().split()))

array.sort()
dist = [0] * (n-1)
for i in range(n-1):
    dist[i] = array[i + 1] - array[i]

dist.sort(reverse=True)
print(sum(dist[k-1:]))