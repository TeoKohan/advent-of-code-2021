I = [line.strip() for line in open('input')]
fish = I[0].split(',')
fish = list(map(lambda n: int(n), fish))
buckets = [0] * 9
for i in range(9):
    buckets[i] = sum([1 for f in fish if f == i])

print(buckets)

for i in range(80):
    newfish = buckets[0]
    for j in range(8):
        buckets[j] = buckets[j+1]
    buckets[8] =  newfish
    buckets[6] += newfish
    
output = open('output', 'w')
output.write(str(sum(buckets)))
output.close()