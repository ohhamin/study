import sys
input = sys.stdin.readline

def binary(x):
    s = 0
    e = len(dp) - 1
    while s <= e:
        mid = (e + s) // 2
        if dp[mid] == x:
            return mid
        elif dp[mid] < x:
            s = mid + 1
        else:
            e = mid - 1
    return s

array = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
array.sort(key = lambda x:x[0])

dp = [-1]
dp_idx = []

for i in array:
    if dp[-1] < i[1]:
        dp.append(i[1])
        dp_idx.append((len(dp) - 2, i[1]))
    else:
        idx = binary(i[1])
        dp[idx] = i[1]
        dp_idx.append((idx - 1, i[1]))

last_idx = len(dp) - 2

result = []
for i in dp_idx[::-1]:
    if i[0] == last_idx:
        result.append(i[1])
        last_idx -= 1

print(n - len(result))
for i in array:
    if i[1] not in result:
        print(i[0])