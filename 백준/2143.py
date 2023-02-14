# from collections import defaultdict

# t = int(input())
# n = int(input())
# n_array = list(map(int, input().split()))
# m = int(input())
# m_array = list(map(int, input().split()))

# dic1 = defaultdict(int)
# for i in range(n):
#     for j in range(i+1, n+1):
#         dic1[sum(n_array[i:j])] += 1
# result = 0
# for i in range(m):
#     for j in range(i+1, m+1):
#         result += dic1[t - sum(m_array[i:j])]

# print(result)

import bisect

t = int(input())
n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))
n_sum = []
m_sum = []

for i in range(n):
    n_sum.append(n_array[i])
    for j in range(i+1, n):
        n_sum.append(n_sum[-1] + n_array[j])
for i in range(m):
    m_sum.append(m_array[i])
    for j in range(i+1, m):
        m_sum.append(m_sum[-1] + m_array[j])
n_sum.sort()
m_sum.sort()
result = 0
for i in n_sum:
    result += (bisect.bisect_right(m_sum, t-i) - bisect.bisect_left(m_sum, t-i))
print(result)