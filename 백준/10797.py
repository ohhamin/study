n = int(input())
array = list(map(int, input().split()))
result = 0
for i in array:
    if n == i:
        result += 1
print(result)