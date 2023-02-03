import bisect

n = int(input())
array = list(map(int, input().split()))

dp = []
check = []
for i in array:
    if not dp:
        dp.append(i)
        check.append((1, i))
    else:
        if dp[-1] < i:
            dp.append(i)
            check.append((len(dp), i))
        else:
            idx = bisect.bisect_left(dp, i)
            dp[idx] = i
            check.append((idx + 1, i))
            
result = []
last_idx = len(dp)
for i in check[::-1]:
    if i[0] == last_idx:
        result.append(i[1])
        last_idx -= 1

print(len(result))
print(*result[::-1])
