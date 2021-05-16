import sys

new_words = set([x[17:-6] for x in ''.join(sys.argv[1]).split('|')])
print(new_words,'\n')
print(''.join(sys.argv[1]).split('|'))
existing_words = set([x.rstrip() for x in open('magyar_szavak.txt', 'r', encoding = 'utf-8').readlines()])


with open('magyar_szavak.txt', 'w', encoding = 'utf-8') as f:
    for i in existing_words.union(new_words):
        f.write(f'{i}\n')
