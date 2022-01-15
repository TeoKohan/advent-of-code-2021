from collections import Counter

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

class Cube:

    def __init__(self, bool, start, end):
        self.bool  = bool
        self.start = start
        self.end   = end

    def __iter__(self):
        return iter([self.bool, self.start, self.end])

    def __str__(self):
        return '(' + ('fill' if self.bool else 'empty') + ', ' + str(self.start) + ', ' + str(self.end) + ')'

P = Point(1, 3, 7)
print(P)

I = [line.strip() for line in open('input')]

L = [[W for W in L.split('=')] for L in I ]
L = [(V[:-2], X[:-2], Y[:-2], Z) for V, X, Y, Z in L]
L = [(V == 'on', X.split('..'), Y.split('..'), Z.split('..')) for V, X, Y, Z in L]
L = [(V, range(*map(int, X)), range(*map(int, Y)), range(*map(int, Z))) for V, X, Y, Z in L]
L = [(Cube(V, Point(X.start, Y.start, Z.start), Point(X.stop, Y.stop, Z.stop))) for V, X, Y, Z in L]

C = {(x, y, z): False for x in range(-50, 51) for y in range(-50, 51) for z in range(-50, 51)}

for V, (a,b,c), (d,e,f) in L:
    x = range(max(-50, a), min(50, d)+1)
    y = range(max(-50, b), min(50, e)+1)
    z = range(max(-50, c), min(50, f)+1)
    for (u, v, w) in [(u, v, w) for u in x for v in y for w in z]:
        C[(u, v, w)] = V

print(sum([1 for v in C.values() if v]))

def intersect(A, B):
    V = not (A.bool)
    print(V)
    start = Point(max(A.start.x, B.start.x), max(A.start.y, B.start.y), max(A.start.z, B.start.z))
    print(A.start)
    end   = Point(max(A.end.x,   B.end.x  ), max(A.end.y  , B.end.y  ), max(A.end.z  , B.end.z  ))
    return Cube(V, start, end)

A = Cube(True, Point(0, 0, 0), Point(5, 5, 5))
B = Cube(True, Point(0, 0, 0), Point(10, 10, 10))
C = intersect(A, B)
print(C)