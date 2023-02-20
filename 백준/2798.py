from itertools import combinations

n, m = map(int, input().split())
array = list(map(int, input().split()))
comb = combinations(array, 3)
result = 0
for i in comb:
    if sum(i) <= m:
        result = max(result, sum(i))
print(result)