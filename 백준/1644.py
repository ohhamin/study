n = int(input())
prime_num =[0, 0] + [1] * (n-1)
prime_nums = []
for i in range(2, n+1):
    if prime_num[i] == 1:
        prime_nums.append(i)
        for j in range(2*i, n+1, i):
            prime_num[j] = 0
s, e = 0, 0
if n == 1:
    print(0)
else:
    now = prime_nums[0]
    count = 0
    while e >= s:
        if now == n:
            count += 1
        if now <= n:
            e += 1
            if len(prime_nums) == e:
                break
            now += prime_nums[e]
        else:
            now -= prime_nums[s]
            s += 1

    print(count)