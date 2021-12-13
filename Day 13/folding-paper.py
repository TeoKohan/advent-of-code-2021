I = [line.strip() for line in open('input')]
(D, F) = (I[:1004], I[1005:])

D = [line.split(',') for line in D]
D = [(int(a), int(b)) for (a, b) in D]
M = (max(D, key = lambda x: x[0])[0], max(D, key = lambda x: x[1])[1])
M = [[False for x in range(max(D, key = lambda x: x[0])[0]+1)] for y in range(max(D, key = lambda x: x[1])[1]+1)]
for (x, y) in D:
    M[y][x] = True

F = [(line.split('=')[0][-1], int(line.split('=')[1])) for line in F]
print(F)

def parts(direction, fold_line, P):
    if direction == 'x':
        (A, B) = ([L[:fold_line] for L in P], [L[fold_line+1:] for L in P])
        return (A, B)
    if direction == 'y':
        (A, B) = (P[:fold_line], P[fold_line+1:])
        return (A, B)

def extend(direction, B, A):
    if direction == 'x':
        L = len(A[0]) - len(B[0]) 
        B = [[False] * L + line for line in B]
        return B
    if direction == 'y':
        L = len(A) - len(B)
        B = [[False] * len(B[0])] * L + B
        return B

def compose(A, B):
    return [[A[y][x] or B[y][x] for x in range(len(A[0]))] for y in range(len(A))]

def fold(direction, fold_line, P):
    (A, B) = parts(direction, fold_line, P)
    if direction == 'x':
        B = [list(reversed(line)) for line in B]
    if direction == 'y':
        B = list(reversed(B))
    B = extend(direction, B, A)
    return compose(A, B)

A = fold(F[0][0], F[0][1], M)
one_fold = (sum([1 for line in A for cell in line if cell]))

A = M
for (direction, fold_line) in F:
    A = fold(direction, fold_line, A)

O = [['█' if cell else ' ' for cell in line] for line in A]
O = [''.join(line) for line in O]
O = '\n'.join(O)

output = open('output', 'w')
output.write(str(one_fold)+'\n'+ O +'\n')
output.close()