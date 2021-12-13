I = [line.strip() for line in open('input')]

D = { }
for line in I:
    (S, E) = line.split('-')
    if S in D:
        D[S] += [E]
    else:
        D[S] = [E]
    if E in D:
        D[E] += [S]
    else:
        D[E] = [S]

def move_cave(PS):
    QS = []
    for (P, B) in PS:
        position = P[-1]
        if position == 'end':
            QS.append((P, B))
            continue
        available = D[position]
        available = [cave for cave in available if (cave.isupper()) or (cave not in P) or (cave not in ['start', 'end'] and B) ]
        for cave in available:
            QS.append( (P+[cave], B and (cave.isupper() or cave not in P)) )
    return QS

C = [(['start'], False)]
while(next((P for (P, B) in C if P[-1] != 'end'), None) != None):
    C = move_cave(C)
simple_path = (len(C))

C = [(['start'], True)]
while(next((P for (P, B) in C if P[-1] != 'end'), None) != None):
    C = move_cave(C)
repeat_path = (len(C))

output = open('output', 'w')
output.write(str(simple_path)+'\n'+str(repeat_path)+'\n')
output.close()