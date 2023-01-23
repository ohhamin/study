while 1:
    word = input()
    if word == 'END':
        break
    reverse_word = ''
    for i in word:
        reverse_word = i + reverse_word
    print(reverse_word)