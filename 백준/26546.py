n = int(input())
for _ in range(n):
    word, s, e = list(input().split())
    result = word[0:int(s)] + word[int(e):]
    print(result)