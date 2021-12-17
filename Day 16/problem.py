from math import ceil, prod
from enum import Enum

I = [line.strip() for line in open('input')]

T = {
    '0': '0000', '1': '0001', '2': '0010',
    '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110',
    'F': '1111'
}

def pad4l(S):
    return S.zfill((ceil(len(S)/4)*4))

def pad4r(S):
    return S.ljust((ceil(len(S)/4)*4), '0')

def h2b(H):
    return ''.join([T[c] for c in H])

def b2h(B):
    IT = {v: k for k, v in T.items()}
    B = pad4r(B)
    B = [''.join(B[i:i+4]) for i in range(0, len(B), 4)]
    return ''.join([IT[c] for c in B])

def parse_header(P):
    version = int(P[:3] , base = 2)
    type    = int(P[3:6], base = 2)
    content = P[6:]
    return version, type, content

def parse_literal(v, t, P):
    number = ''
    i = 0
    while P[i*5] == '1':
        number += P[i*5+1:i*5+5]
        i += 1
    number += P[i*5+1:i*5+5]
    return [v], [t], int(number, base = 2), P[(i+1)*5:]

def parse_subpacket(v, t, P):
    length_type = P[0]

    output = {
        'version': [v],
        'type':    [t],
        'value':   []
    }

    def register_subpacket(subpacket):
        sv, st, R, subpacket = parse_packet(subpacket)
        output['version'] += sv
        output['type']    += st
        output['value']   += [R]
        return subpacket

    if length_type == '0':
        bit_length = int(P[1:16], base = 2)
        subpackets, P = P[16:16+bit_length], P[16+bit_length:]
        while len(subpackets) > 0:
            subpackets = register_subpacket(subpackets)
    else:
        packet_length, P = int(P[1:12], base = 2), P[12:]
        for _ in range(packet_length):
            P = register_subpacket(P)

    OP = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        4: lambda x: x,
        5: lambda x: 1 if x[0] >  x[1] else 0,
        6: lambda x: 1 if x[0] <  x[1] else 0,
        7: lambda x: 1 if x[0] == x[1] else 0
    }

    return output['version'], output['type'], OP[t](output['value']), P     

def parse_packet(P):
    v, t, P = parse_header(P)
    if t == 4:
        return parse_literal(v, t, P)
    else:
        return parse_subpacket(v, t, P)

OP = {
    'sum': 0,
    'prod': 1,
    'min': 2,
    'max': 3,
    'literal': 4,
    'gt': 5,
    'lt': 6,
    'eq': 7
}

def make_packet(literal = 0, version = 1, operation = 'literal', length_type = 1, packets = []):

    operation = OP[operation]
    version = bin(version)[2:].zfill(3)
    operation = bin(operation)[2:].zfill(3)
    literal = bin(literal)[2:]
    if operation == '100':
        literal = [pad4l(literal[i:i+4]) for i in range(0, len(literal), 4)]
        literal = ['1'+b for b in literal]
        literal[-1] = '0' + literal[-1][1:]
        literal = ''.join(literal)
        return version+operation+literal
    else:
        packets = [make_packet(literal=P) if type(P) == int else P for P in packets]
        length = sum([len(P) for P in packets]) if length_type in ['0', 0] else len(packets)
        length = bin(length)[2:].zfill(15 if length_type in ['0', 0] else 11)
        print(packets)
        return version + operation + str(length_type) + length + ''.join(packets)
        
    

B = h2b(I[0])
v, t, S, P = parse_packet(B)

output = open('output', 'w')
output.write(str(sum(v))+'\n'+ str(S) +'\n')
output.close()

#make a packet
#product = make_packet(operation='sum', packets=[5, make_packet(operation='prod', packets=[9, 6]), 10])