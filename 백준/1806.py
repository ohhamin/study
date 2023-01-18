n, s = map(int, input().split())
array = list(map(int, input().split()))

result = 100001
tmp_sum = 0
start, end = 0, 0

while 1:
    if tmp_sum >= s:
        if result >= end - start:
            result = end - start
        tmp_sum -= array[start]
        start += 1
    elif end == n:
        break
    else:
        tmp_sum += array[end]
        end += 1

if result == 100001:
    print(0)
else:
    print(result)