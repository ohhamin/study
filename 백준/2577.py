a = int(input())
b = int(input())
c = int(input())
result = a * b * c
array = [0] * 10
for i in str(result):
    array[int(i)] += 1
for i in array:
    print(i)