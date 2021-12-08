I = [line.strip() for line in open('input')]
O = list(map(lambda x: (x.split('|'))[1].strip(), I))
O = list(map(lambda x: x.split(), O))
O = [i for output in O for i in output]
C = [1 for v in O if (len(v) in [2, 4, 3, 7]) ]

print (sum(C))