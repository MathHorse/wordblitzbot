new_words = []
with open(input('Source: '), 'r', encoding = 'utf-8') as f:
    for line in f:
        for word in line.split():
           new_words.append(word)
new_words = set(new_words)
existing_words = set([x.strip('\n') for x in open('magyar_szavak.txt', 'r', encoding = 'utf-8').readlines()])

for word in new_words:
    if word == '':
        word.remove(word)

with open('magyar_szavak.txt', 'w', encoding = 'utf-8') as f:
    for i in existing_words.union(new_words):
        f.write(f'{i}\n')
