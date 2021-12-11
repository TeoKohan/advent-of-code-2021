I = [line.strip() for line in open('input')]
I = [[int(n) for n in line] for line in I]

D = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def advance(I):
    I = [[n+1 for n in line] for line in I]
    (I, F) = update(I, [[True for x in range(10)] for y in range(10)])

    return (I, sum([1 for line in F for cell in line if not cell]))

def update(I, F):
    Y = [line[:] for line in I]
    for (x, y) in [(x, y) for x in range(10) for y in range(10)]:
        if Y[y][x] > 9:
            F[y][x] = False
            Y[y][x] = 0
            N = []
            for (u, v) in D:
                if 0 <= x + u < 10 and 0 <= y + v < 10:
                    N.append((x + u, y + v))
            for (u, v) in N:
                if F[v][u]:
                    Y[v][u] += 1
    if I != Y:
        return update(Y, F)
    return (Y, F)

M = [line[:] for line in I]
flashes = 0
for i in range(100):
    (M, F) = advance(M)
    flashes += F

M = [line[:] for line in I]
mega_flash = False
round = 1
while not mega_flash:
    (M, F) = advance(M)
    if F == 100:
        mega_flash = round
    round += 1

output = open('output', 'w')
output.write(str(flashes)+'\n'+str(mega_flash)+'\n')
output.close()