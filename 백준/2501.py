n, k = map(int, input().split())
result = []
for i in range(1, n+1):
    if n % i == 0:
        result.append(i)
try:
    print(result[k-1])
except:
    print(0)