ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
if ay >= cy:
    print(abs(az - cx), ay // cy, abs(ax - cz))
else:
    print(abs(az - cx), cy // ay, abs(ax - cz))