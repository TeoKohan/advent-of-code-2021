I = [line.strip() for line in open('input')]

def sign(n):
    if n == 0:
        return 0
    if n > 0:
        return 1
    return -1

def parse(line):
    (a, b) = line.split('->')
    (a, b) = (a.strip(), b.strip())
    ((u, v), (w, z)) = (a.split(','), b.split(','))
    (u, v, w, z) = (int(u), int(v), int(w), int(z))
    return (u, v, w, z)

lines = list(map(parse, I))
underwater = [[0 for x in range(1000)] for y in range(1000)] 

def get_cells(u, v, w, z):
    cells = []
    length = max(abs(w-u), abs(z-v))+1
    (dx, dy) = (sign(w-u), sign(z-v))
    cells = [(u + r * dx, v + r * dy) for r in range(length)]
    return cells

for line in lines:
    (u, v, w, z) = line
    if u == w or v == z:
        for cell in get_cells(u, v, w, z):
            underwater[cell[0]][cell[1]] += 1

linear_sum = sum([1 for row in underwater for cell in row if cell > 1])

underwater = [[0 for x in range(1000)] for y in range(1000)] 

for line in lines:
    (u, v, w, z) = line
    for cell in get_cells(u, v, w, z):
        underwater[cell[0]][cell[1]] += 1


diagonal_sum = sum([1 for row in underwater for cell in row if cell > 1])

output = open('output', 'w')
output.write(str(linear_sum)+'\n'+str(diagonal_sum)+'\n')
output.close()