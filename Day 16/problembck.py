from math import prod

I = [line.strip() for line in open('input')]
D = {
    'version' : 0
}

def h2b(H):
    D = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    return ''.join([D[c] for c in H])

def header(P):
    version = int(P[:3] , base=2)
    type    = int(P[3:6], base=2)
    content = P[6:]
    return version, type, content

def parse_literal(P):
    number = ''
    i = 0
    while P[i*5] == '1':
        number += P[i*5+1:i*5+5]
        i += 1
    number += P[i*5+1:i*5+5]
    return int(number, base = 2), P[(i+1)*5:]

def parse_subpacket(P, t):
    length_type = P[0]
    if length_type == '0':
        bit_length = int(P[1:16], base = 2)
        subpackets = P[16:16+bit_length]
        P = P[16+bit_length:]
        results = []
        while len(subpackets) > 0:
            R, subpackets = parse_packet(subpackets)
            results.append(R)
    else:
        packet_length = int(P[1:12], base = 2)
        P = P[12:]
        results = []
        for _ in range(packet_length):
            R, P = parse_packet(P)
            results.append(R)

    OP = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda x: 1 if x[0] >  x[1] else 0,
        6: lambda x: 1 if x[0] <  x[1] else 0,
        7: lambda x: 1 if x[0] == x[1] else 0
    }

    return OP[t](results), P
        

def parse_packet(P):
    v, t, P = header(P)
    D['version'] += v
    if t == 4:
        return parse_literal(P)
    else:
        return parse_subpacket(P, t)

test_literal = 'C200B40A82'
B = h2b(I[0])
S, P = parse_packet(B)
print(D['version'])
print(S)
output = open('output', 'w')
output.write(str(1)+'\n'+ str(2) +'\n')
output.close()