import sys
input = sys.stdin.readline

n, k = map(int, input().split())
time = [0] * n
for i in range(n):
    time[i] = int(input())

diff = [0] * (n - 1)
for i in range(n-1):
    diff[i] = time[i + 1] - time[i]

diff.sort(reverse=True)
print(sum(diff[k-1:]) + k)
