import sys
input = sys.stdin.readline

def dfs(now_dic, word, n):
    global dash
    print(n * dash + word)
    for i in sorted(now_dic[word]):
        dfs(now_dic[word], i, n + 1)

n = int(input())
dic = dict()
dash = '--'
for _ in range(n):
    a = list(input().split())
    now = dic
    for i in range(int(a[0])):
        try:
            now = now[a[i + 1]]
        except:
            now[a[i + 1]] = dict()
            now = now[a[i + 1]]

for i in sorted(dic):
    dfs(dic, i, 0)