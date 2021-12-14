I = [line.strip() for line in open('input')]

F = I[0]
T = I[2:]

D = [[x.strip() for x in L.split('->')] for L in T]
D = {x: y for (x, y) in D}

def quantize(F):
    D = { }
    for i in range(len(F)-1):
        k = F[i:i+2]
        if (k in D):
            D[k] += 1
        else:
            D[k] =  1
    return D

def apply(F, D):
    G = { }
    for k in F:
        c = D[k]
        if k[0]+c in G:
            G[k[0]+c] += F[k]
        else:
            G[k[0]+c] = F[k]
        if c+k[1] in G:
            G[c+k[1]] += F[k]
        else:
            G[c+k[1]] = F[k]
    return G

def count(F):
    G = { }
    for k in F:
        for c in k:
            if c in G:
                G[c] += F[k]
            else:
                G[c] = F[k]
    for k in G:
        G[k] //= 2
    G['O'] += 1
    G['F'] += 1
    return G

F = quantize(F)

E = { } | F
for i in range(10):
    E = apply(E, D)
G = count(E)

ten = max(G.values()) - min(G.values())

E = { } | F
for i in range(40):
    E = apply(E, D)
G = count(E)

forty = max(G.values()) - min(G.values())

output = open('output', 'w')
output.write(str(ten)+'\n'+ str(forty) +'\n')
output.close()