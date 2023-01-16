n = int(input())
array = list(map(int, input().split()))


def binarySearch(x):
    global resultLen
    s = 0
    e = resultLen - 1
    while s <= e:
        mid = (s + e) // 2
        if result[mid] == x:
            return mid
        elif result[mid] < x:
            s = mid + 1
        else:
            e = mid - 1
    return s

result = [array[0]]
resultLen = 1

for i in array:
    if result[-1] < i:
        result.append(i)
        resultLen += 1
    else:
        idx = binarySearch(i)
        result[idx] = i
print(resultLen)