I = [line.strip() for line in open('input')]

I = [line.strip() for line in open('input')]
O = [(x.split('|'))[1].strip() for x in I]
O = [x.split() for x in O]
O = [i for output in O for i in output]
C = [1 for v in O if (len(v) in [2, 3, 4, 7]) ]

simple = sum(C)

S = [(x.split('|'))[0].strip() for x in I]
O = [(x.split('|'))[1].strip() for x in I]
S = [x.split() for x in S]
O = [x.split() for x in O]

numbers = [
    set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    set(['c', 'f']),
    set(['a', 'c', 'd', 'e', 'g']),
    set(['a', 'c', 'd', 'f', 'g']),
    set(['b', 'c', 'd', 'f']),
    set(['a', 'b', 'd', 'f', 'g']),
    set(['a', 'b', 'd', 'e', 'f', 'g']),
    set(['a', 'c', 'f']),
    set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    set(['a', 'b', 'c', 'd', 'f', 'g'])
]

complex = 0
for i in range(len(S)):
    SS = S[i]
    one   = [n for n in SS if len(n) == 2][0]
    four  = [n for n in SS if len(n) == 4][0]
    seven = [n for n in SS if len(n) == 3][0]
    eight = [n for n in SS if len(n) == 7][0]
    one_apparitions = [len([n for n in SS if one[0] in n]),
                       len([n for n in SS if one[1] in n])]
    c = one[0] if one_apparitions[0] == 8 else one[1]
    f = one[0] if one_apparitions[0] == 9 else one[1]
    a = [n for n in seven if n not in [c, f]][0]
    four = [n for n in four if n not in [c, f]]
    four_apparitions = [len([n for n in SS if four[0] in n]),
                        len([n for n in SS if four[1] in n])]
    b = four[0] if four_apparitions[0] == 6 else four[1]
    d = four[0] if four_apparitions[0] == 7 else four[1]
    eight = [n for n in eight if n not in [a, b, c, d, f]]
    eight_apparitions = [len([n for n in SS if eight[0] in n]),
                         len([n for n in SS if eight[1] in n])]
    e = eight[0] if eight_apparitions[0] == 4 else eight[1]
    g = eight[0] if eight_apparitions[0] == 7 else eight[1]
    #Decoding done
    OO = O[i]
    dictionary = {
        a: 'a',
        b: 'b',
        c: 'c',
        d: 'd',
        e: 'e',
        f: 'f',
        g: 'g'
    }
    translation = [[dictionary[y] for y in x] for x in OO]
    translation = [set(x) for x in translation]
    password = [0] * 4
    for j in range(4):
        for k in range(10):
            if translation[j] == numbers[k]:
                password[j] = k
    password = int(''.join([str(x) for x in password]))
    complex += password

output = open('output', 'w')
output.write(str(simple)+'\n'+str(complex)+'\n')
output.close()