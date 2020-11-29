paths = [[y.split(',') for y in x.split(';')[:-1]] for x in open('paths.txt', 'r').readlines()[:-1]]
letters = [x.split(',') for x in open('letters.txt', 'r', encoding = 'utf-8').read().split(';')]
words = [x.strip('\n') for x in open('magyar_szavak.txt', 'r').readlines()]

for path in paths:
    word = ''
    for tile in path:
        word += letters[int(tile[0])][int(tile[1])]
    if word in words:
        print(word)
