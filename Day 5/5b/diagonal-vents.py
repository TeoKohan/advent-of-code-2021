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
n = 1000
underwater = [[0 for x in range(n)] for y in range(n)] 

for line in lines:
    cells = []
    #Is horizontal or vertical
    (u, v, w, z) = line
    length = max(abs(w-u), abs(z-v))+1
    (dx, dy) = (sign(w-u), sign(z-v))
    cells = [(u + r * dx, v + r * dy) for r in range(length)]
    for cell in cells:
        underwater[cell[0]][cell[1]] += 1

sum = sum([1 for row in underwater for cell in row if cell > 1])

output = open('output', 'w')
output.write(str(sum))
output.close()