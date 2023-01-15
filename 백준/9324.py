from collections import defaultdict

t = int(input())

for tc in range(t):
    word = input()
    dic = defaultdict(int)
    flag = 0
    for i in range(len(word)):
        dic[word[i]] += 1
        if dic[word[i]] == 3:
            if i + 1 == len(word) or word[i + 1] != word[i]:
                flag = 1
                break
            dic[word[i]] = -1
    if flag == 1:
        print('FAKE')
    else:
        print('OK')