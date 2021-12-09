I = [line.strip() for line in open('input')]
I = [[int(n) for n in line] for line in I]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
L = []
def is_low_point(x, y):
    N = []
    for (u, v) in D:
        if 0 <= x+u < 100 and 0 <= y+v < 100:
            N.append((x+u, y+v))
    if min([I[v][u] for (u, v) in N]) > I[y][x]:
        return True
    return False

for (x, y) in [(x, y) for x in range(100) for y in range(100)]:
    if is_low_point(x, y):
        L.append((x, y))

basin_size = { }
for (x, y) in L:
    basin_size[str(x)+'|'+str(y)] = 0

def find_lowest_point(x, y):
    if (is_low_point(x, y)):
        return (x, y)
    else:
        N = []
        for (u, v) in D:
            if 0 <= x+u < 100 and 0 <= y+v < 100:
                N.append((x+u, y+v))
        (u, v) = min(N, key = lambda t: I[t[1]][t[0]])
        return find_lowest_point(u, v)

for (x, y) in [(x, y) for x in range(100) for y in range(100)]:
    if I[y][x] != 9:
        (u, v) = find_lowest_point(x, y)
        basin_size[str(u)+'|'+str(v)] += 1


danger = [I[v][u]+1 for (u, v) in L]

biggest_basins = sorted(basin_size.values())
biggest_basins = biggest_basins[-3:]

output = open('output', 'w')
output.write(str(sum(danger))+'\n'+str(biggest_basins[0] * biggest_basins[1] * biggest_basins[2])+'\n')
output.close()