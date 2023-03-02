n = int(input())
a, b, c = map(int, input().split())
print(min(n, a) + min(n, b) + min(n, c))