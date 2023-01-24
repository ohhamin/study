import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [0] + list(map(int, input().split()))
sum_array = [0] * (n + 1)
for i in range(1, n + 1):
    sum_array[i] = sum_array[i-1] + array[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_array[j] - sum_array[i-1])