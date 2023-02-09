n = int(input())
array = list(map(int, input().split()))
sums = [0] * (n+1)
for i in range(n):
    sums[i+1] = sums[i] + array[i]
result = 0
for i in range(1, n):
    result += array[i-1] * (sums[-1] - sums[i])
print(result)