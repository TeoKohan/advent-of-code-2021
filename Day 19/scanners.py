from itertools import combinations
I = [line.strip() for line in open('input')]

M = [[1,2,3],[4,5,6],[7,8,9]]

def orientations(M):
    def rotations(MS, n):
        def invert(M):
            return [-m for m in M]

        R = []
        for M in MS:
            C = combinations(range(3), n)
            R += [[ invert(M[i]) if i in c else M[i] for i in range(3) ] for c in C]
        return R

    M = list(zip(*M))
    O = [
        [M[0], M[2], M[1]],
        [M[1], M[0], M[2]],
        [M[2], M[1], M[0]]
    ]
    E = [
        [M[0], M[1], M[2]],
        [M[1], M[2], M[0]],
        [M[2], M[0], M[1]]
    ]

    return [list(zip(*M)) for M in rotations(E, 0) + rotations(O, 1) + rotations(E, 2) + rotations(O, 3)]

M = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3],
]

M = orientations(M)

print(len(M), M)