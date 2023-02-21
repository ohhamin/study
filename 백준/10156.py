k, n, m = map(int, input().split())
need = k * n
if m < need:
    print(need - m)
else:
    print(0)