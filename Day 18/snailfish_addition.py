from copy import deepcopy

I = [line.strip() for line in open('input')]

def snailfish_parse(A):
    if A.isnumeric():
        return int(A)

    def find_split(A):
        nest = 0
        for i in range(len(A)):
            nest += 1 if A[i] == '[' else -1 if A[i] == ']' else 0
            if A[i] == ',' and nest == 0:
                return i

    A = A[1:-1]
    i = find_split(A)
    left, right = A[:i], A[i+1:]
    return [snailfish_parse(left), snailfish_parse(right)]

def snailfish_depth(S, M=[], n=0):
        if type(S) is int:
            return []
        else:
            if n > 3:
                return [M]
            x, y = S
            return snailfish_depth(x, M+[0], n+1) + snailfish_depth(y, M+[1], n+1)

def snailfish_value(S, M=[]):
        if type(S) is int:
            if S >= 10:
                return [M]
            else:
                return []
        else:
            x, y = S
            return snailfish_value(x, M+[0]) + snailfish_value(y, M+[1])

def snailfish_add(A, B):
    return [A] + [B]

def snailfish_reduce(A):
    def retrieve(A, M):
            if M == []:
                return A
            return A[M[0]] if len(M) == 1 else retrieve(A[M[0]], M[1:])

    def explode(A, M):
        def fork(M, dir):
            if M == []:
                return []
            return M[:-1]+[dir] if M[-1] != dir else fork(M[:-1], dir)

        def walk(A, M, dir):
            if M != []:
                B = A[:]
                B = retrieve(B, M)
                while type(B) != int:
                    B = B[dir]
                    M += [dir]
            return M

        x, y = retrieve(A, M)
        l, r = walk(A, fork(M, 0), 1), walk(A, fork(M, 1), 0)
        for m, v in [(m, v) for m, v in [(l, x), (r, y)] if m != []]:
            retrieve(A, m[:-1])[m[-1]] += v
        retrieve(A, M[:-1])[M[-1]] = 0

    def split(A, M):
        n = retrieve(A, M)
        retrieve(A, M[:-1])[M[-1]] = [n//2, n//2+n%2]
    
    M = snailfish_depth(A)[0] if snailfish_depth(A) != [] else None
    if M != None:
        explode(A, M)
        snailfish_reduce(A)

    M = snailfish_value(A)[0] if snailfish_value(A) != [] else None
    if M != None:
        split(A, M)
        snailfish_reduce(A)
    
def magnitude(A):
    if type(A) == int:
        return A
    else:
        x, y = A
        return 3 * magnitude(x) + 2 * magnitude(y)

L = [snailfish_parse(l) for l in I]
S = deepcopy(L[0])
for A in L[1:]:
    S = snailfish_add(S, deepcopy(A))
    snailfish_reduce(S)
homework_magnitude = magnitude(S)

M = []
L = [snailfish_parse(l) for l in I]
for A, B in [(A, B) for A in L for B in L if A != B]:
    S = snailfish_add(deepcopy(A), deepcopy(B))
    snailfish_reduce(S)
    M += [magnitude(S)]

output = open('output', 'w')
output.write(str(homework_magnitude)+'\n'+ str(max(M)) +'\n')
output.close()