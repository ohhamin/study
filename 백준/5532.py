l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e, f = 0, 0
if a % c: e = 1
if b % d: f = 1
print(l - max(a // c + e, b // d + f))