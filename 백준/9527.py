import math

def count(x):
    bin_x = bin(x)
    len_x = len(bin_x)
    count = 0
    for i in range(2, len_x):
        if bin_x[i] == '1':
            tmp = len_x - i - 1
            count += sums[tmp]
            count += x - 2**(tmp) + 1
            x = x - 2**(tmp)
    return count

a, b = map(int, input().split())
max_bin = int(math.log2(b)) + 1
array = [0 for _ in range(max_bin + 1)]
sums = [0 for _ in range(max_bin + 1)]
array[1] = 1
for i in range(2, max_bin + 1):
    array[i] = array[i-1]*2 + 2**(i-2)
for i in range(1, max_bin + 1):
    sums[i] = sums[i-1] + array[i]
print(count(b) - count(a-1))