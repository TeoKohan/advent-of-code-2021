M = [line.rstrip() for line in open('input')]
D = [[M[i-2], M[i-1], M[i]] for i in range(5, len(M), 3) if 
      M[i-2]+ M[i-1]+ M[i] > M[i-5]+ M[i-4]+ M[i-3]
]

output = open('output', 'w')
output.write(str(len(D)))
output.close()