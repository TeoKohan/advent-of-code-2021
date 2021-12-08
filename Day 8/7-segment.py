I = [line.strip() for line in open('input')]

I = [line.strip() for line in open('input')]
O = list(map(lambda x: (x.split('|'))[1].strip(), I))
O = list(map(lambda x: x.split(), O))
O = [i for output in O for i in output]
C = [1 for v in O if (len(v) in [2, 4, 3, 7]) ]

simple = sum(C)

S = list(map(lambda x: (x.split('|'))[0].strip(), I))
O = list(map(lambda x: (x.split('|'))[1].strip(), I))
S = list(map(lambda x: x.split(), S))
O = list(map(lambda x: x.split(), O))

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
    one   = list(filter(lambda x: len(x) == 2, SS))[0]
    four  = list(filter(lambda x: len(x) == 4, SS))[0]
    seven = list(filter(lambda x: len(x) == 3, SS))[0]
    eight = list(filter(lambda x: len(x) == 7, SS))[0]
    one_apparitions = [len(list(filter(lambda x: one[0] in x, SS))),
                       len(list(filter(lambda x: one[1] in x, SS)))]
    c = one[0] if one_apparitions[0] == 8 else one[1]
    f = one[0] if one_apparitions[0] == 9 else one[1]
    a = list(filter(lambda x: x != c and x != f, seven))[0]
    four = list(filter(lambda x: x != c and x != f, four))
    four_apparitions = [len(list(filter(lambda x: four[0] in x, SS))),
                        len(list(filter(lambda x: four[1] in x, SS)))]
    b = four[0] if four_apparitions[0] == 6 else four[1]
    d = four[0] if four_apparitions[0] == 7 else four[1]
    eight = list(filter(lambda x: x != a and x != b and x != c and x != d and x != f, eight))
    eight_apparitions = [len(list(filter(lambda x: eight[0] in x, SS))),
                         len(list(filter(lambda x: eight[1] in x, SS)))]
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
    translation = list(map(lambda x: set(map(lambda y: dictionary[y], x)), OO))
    password = [0] * 4
    for j in range(4):
        for k in range(10):
            if translation[j] == numbers[k]:
                password[j] = k
    password = int(''.join(list(map(str, password))))
    complex += password

output = open('output', 'w')
output.write(str(simple)+'\n'+str(complex)+'\n')
output.close()