from collections import Counter
from itertools import product

I = [line.strip() for line in open('input')]
A, B = [int(L[-1]) for L in I]
A, B = (A, 0), (B, 0)

def mod1(n, m):
    return m if n % m == 0 else n % m

def move(C, P, D):
    C = mod1(C+D, 10)
    P += C
    return (C, P)

def deterministic_roll(A, B, D, R, P):
    def roll_dice(D, n):
        return mod1(D+n, 1000)
    
    if P == 'A':
        A = move(*A, roll_dice(D, 1) + roll_dice(D, 2) + roll_dice(D, 3))
    else:
        B = move(*B, roll_dice(D, 1) + roll_dice(D, 2) + roll_dice(D, 3))

    return A, B, roll_dice(D, 3), R+3, 'B' if P == 'A' else 'A'

D = 0
R = 0
P = 'A'
while A[1] < 1000 and B[1] < 1000:
    A, B, D, R, P = deterministic_roll(A, B, D, R, P)

loser_times_rolls = min(A[1], B[1]) * R

A, B = [int(L[-1]) for L in I]
A, B = (A, 0), (B, 0)

P = 'A'
dirac = Counter([sum(S) for S in list(product([1,2,3], repeat=3))])
US = Counter()
US[(A, B)] = 1
RS = {
    'A': 0,
    'B': 0
}

def dirac_roll(US, RS, P):
    NU = Counter()
    for k, v in US.items():
        if k[0][1] >= 21 or k[1][1] >= 21:
            RS['A' if k[0][1] >= 21 else 'B'] += v
            continue
        for D, V in dirac.items():
            U = (move(*k[0], D), k[1]) if P == 'A' else (k[0], move(*k[1], D))
            NU[U] += v * V
    return NU, RS, 'B' if P == 'A' else 'A'

while len(US) > 0:
    US, RS, P = dirac_roll(US, RS, P)
    
output = open('output', 'w')
output.write(str(loser_times_rolls)+'\n'+ str(max(RS.values())) +'\n')
output.close()