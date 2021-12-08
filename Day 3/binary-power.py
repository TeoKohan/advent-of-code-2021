from statistics import mode
I = [line.strip() for line in open('input')]

power = [list(i) for i in zip(*I)]

columns = [0] * 12
for i in range(12):
    columns[i] = mode(power[i])
epsilon = int(''.join(columns), 2)
gamma   = epsilon ^ 0xFFF

power_consumption = str(epsilon*gamma)

O2  = I
CO2 = I

for bit in reversed(range(12)):
    mode_O2  = mode([list(i) for i in zip(*O2) ][bit])
    mode_CO2 = mode([list(i) for i in zip(*CO2)][bit])
    if (len(O2) > 1):
        filter(lambda x: x[bit] == mode_O2,   O2)
    if (len(CO2) > 1):
        filter(lambda x: x[bit] != mode_CO2, CO2)

life_support = str(int(O2[0], 2) * int(CO2[0], 2))

output = open('output', 'w')
output.write(power_consumption+'\n'+life_support+'\n')
output.close()