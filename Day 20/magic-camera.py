I = [line.strip() for line in open('input')]
T = [ '1' if c == '#' else '0' for c in I[0] ]

L = [['1' if c == '#' else '0' for c in L] for L in I[2:]]

def get_value(I, x, y):
    D = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    S = ''
    for u, v in D:
        S += I[y+v][x+u] if 0 <= x+u < len(I[0]) and 0 <= y+v < len(I) else B
    return T[int(S, base=2)]

def expand(I, B):
    return [[B for i in range(len(I[0])+2)]] + [[B] + L + [B] for L in I] + [[B for i in range(len(I[0])+2)]]

def enhance (I, B):
    I = expand(I, B)
    N = [L[:] for L in I]
    for x, y in [(x, y) for y in range(len(I)) for x in range(len(I[0]))]:
        N[y][x] = get_value(I, x, y)
    B = T[0] if B == '0' else T[-1]
    return N, B

B = '0'

L, B = enhance(L, B)
L, B = enhance(L, B)

two_enhancements = sum([1 if cell == '1' else 0 for row in L for cell in row])

for _ in range(48):
    L, B = enhance(L, B)

fifty_enhancements = sum([1 if cell == '1' else 0 for row in L for cell in row])

output = open('output', 'w')
output.write(str(two_enhancements)+'\n'+ str(fifty_enhancements) +'\n')
output.close()