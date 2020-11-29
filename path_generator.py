#generate all possible wordpaths on 4*4 grid
f = open('paths.txt', 'a')

def in_square(tile):
    if tile[0] < 0 or tile[0] > 3 or tile[1] < 0 or tile[1] > 3:
        return False
    return True

def paths(prevpath):
    for i in prevpath:
        f.write(f'{i[0]},{i[1]};')
    f.write('\n')

    if len(prevpath) > 8:
        return

    for arr in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        newtile = [prevpath[-1][0] + arr[0], prevpath[-1][1] + arr[1]]
        if (newtile not in prevpath) and in_square(newtile):
            paths(prevpath + [newtile])

for i in [0,1,2,3]:
    for j in [0,1,2,3]:
        paths([[i, j]])

f.close()
