M = [line.strip() for line in open('input')]
M = list(map(lambda x : int(x), M))
A = [1 for i in range(1, len(M)) if M[i] > M[i-1]]
B = [1 for i in range(0, len(M)-3) if 
      M[i+1] + M[i+2] + M[i+3] > M[i] + M[i+1] + M[i+2]
]
output = open('output', 'w')
output.write(str(sum(A))+'\n'+str(sum(B))+'\n')
output.close()