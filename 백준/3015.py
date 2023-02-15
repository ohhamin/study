import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
stack = []
result = 0

for i in array:
    while stack and stack[-1][0] < i:
        result += stack.pop()[1]
    if stack == []:
        stack.append((i, 1))
    else:
        if stack[-1][0] == i:
            count = stack.pop()[1]
            result += count
            if stack:
                result += 1
            stack.append((i, count+1))
        else:
            stack.append((i, 1))
            result += 1
print(result)