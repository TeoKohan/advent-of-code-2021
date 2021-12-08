I = [line.strip() for line in open('input')]
I = I[0].split(',')
I = list(map(int, I))

V = []
print(max(I))
for position in range(max(I)+1):
    sum = 0
    for crab in I:
        n = abs(crab - position)
        sum += int(n * (n+1) / 2)
    V.append(sum)

print (min(V))