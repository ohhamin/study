def call(x):
    if not tree[x]:
        return 0
    else:
        tmp_array = []
        for i in tree[x]:
            tmp_array.append(call(i))
        tmp_array.sort(reverse=True)
        tmp_result = 0
        for i in range(len(tmp_array)):
            tmp_result = max(tmp_result, tmp_array[i] + i + 1)
        return tmp_result
n = int(input())
array = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[array[i]].append(i)
print(call(0))


# def call(x):
#     if not tree[x]:
#         time[x] = 0
#     else:
#         tmp_array = []
#         for i in tree[x]:
#             call(i)
#             tmp_array.append(time[i])

#         tmp_array.sort(reverse=True)
#         tmp_result = 0
#         for i in range(len(tmp_array)):
#             tmp_result = max(tmp_result, tmp_array[i] + i + 1)
#         time[x] = tmp_result
        
# n = int(input())
# array = list(map(int, input().split()))
# tree = [[] for _ in range(n)]
# time = [0 for _ in range(n)]
# for i in range(1, n):
#     tree[array[i]].append(i)
# call(0)
# print(time[0])