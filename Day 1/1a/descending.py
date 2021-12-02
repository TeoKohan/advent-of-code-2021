M = [line.rstrip() for line in open('input')]
D = [M[i] for i in range(1, len(M)) if int(M[i]) > int(M[i-1])]

output = open('output', 'w')
output.write(str(len(D)))
output.close()