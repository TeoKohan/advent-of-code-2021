I = [line.rstrip() for line in open('input')]
h = 0
d = 0
for line in I:
    (D, A) = line.split()
    if D == 'forward':
        h += int(A)
    if D == 'up':
        d -= int(A)
    if D == 'down':
        d += int(A)

output = open('output', 'w')
output.write(str(h * d))
output.close()