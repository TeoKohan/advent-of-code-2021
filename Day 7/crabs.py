I = [line.strip() for line in open('input')]
I = I[0].split(',')
I = list(map(int, I))

V = []
W = []
print(max(I))
for position in range(max(I)+1):
    sum = [0, 0]
    for crab in I:
        n = abs(crab - position)
        sum[0] += n
        sum[1] += int(n * (n+1) / 2)
    V.append(sum[0])
    W.append(sum[1])

output = open('output', 'w')
output.write(str(min(V))+'\n'+str(min(W))+'\n')
output.close()