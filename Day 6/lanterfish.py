I = [line.strip() for line in open('input')]
fish = I[0].split(',')
fish = list(map(lambda n: int(n), fish))
buckets = [0] * 9
for i in range(9):
    buckets[i] = sum([1 for f in fish if f == i])

def simulate_fish(d):
    b = buckets[:]
    for i in range(d):
        newfish = b[0]
        for j in range(8):
            b[j] = b[j+1]
        b[8] =  newfish
        b[6] += newfish
    return sum(b)

mortal   = simulate_fish(80 )
immortal = simulate_fish(256)

output = open('output', 'w')
output.write(str(mortal)+'\n'+str(immortal)+'\n')
output.close()