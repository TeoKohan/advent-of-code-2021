I = [line.strip() for line in open('input')]

def parse(line):
    (a, b) = line.split('->')
    (a, b) = (a.strip(), b.strip())
    ((u, v), (w, z)) = (a.split(','), b.split(','))
    ((u, v), (w, z)) = ((min(int(u), int(w)), min(int(v), int(z))), (max(int(u), int(w)), max(int(v), int(z))))
    return ((u, v), (w, z))

lines = list(map(parse, I))

n = 1000
underwater = [[0 for x in range(n)] for y in range(n)] 

for line in lines:
    cells = []
    #Is horizontal or vertical
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        cells = [(x, y) for x in range(int(line[0][0]), int(line[1][0])+1) for y in range(int(line[0][1]), int(line[1][1])+1)]
    for cell in cells:
        underwater[cell[0]][cell[1]] += 1

sum = sum([1 for row in underwater for cell in row if cell > 1])

output = open('output', 'w')
output.write(str(sum))
output.close()