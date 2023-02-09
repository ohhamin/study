n, m = map(int, input().split())
array = list(map(int, input().split()))
sums = [0] * (n+1)
remain = [0] * m
result = 0

for i in range(n):
    sums[i+1] = sums[i] + array[i]

for i in range(1, n+1):
    tmp_remain = sums[i] % m
    if tmp_remain == 0:
        remain[tmp_remain] += 1
        result += remain[tmp_remain]
    else:
        result += remain[tmp_remain]
        remain[tmp_remain] += 1
print(result)