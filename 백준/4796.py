cases = 1

while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    result = v // p * l
    if v % p >= l:
        result += l
    else:
        result += v % p
    print("Case %d: %d" %(cases, result))
    cases += 1