I = [line.rstrip() for line in open('input')]
a = 0
h = 0
d = 0
for line in I:
    (D, A) = line.split()
    if D == 'forward':
        h += int(A)
        d += a * int(A)
    if D == 'up':
        a -= int(A)
    if D == 'down':
        a += int(A)

output = open('output', 'w')
output.write(str(h * d))
output.close()