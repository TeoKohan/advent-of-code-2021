I = [line.strip() for line in open('input')]

def simple(I):
    h = 0
    d = 0
    for line in I:
        (D, A) = line.split()
        A = int(A)
        if D == 'forward':
            h += A
        if D == 'up':
            d -= A
        if D == 'down':
            d += A
    print(str(h) + " " + str(d))
    return h * d
        
def aim(I):
    a = 0
    h = 0
    d = 0
    for line in I:
        (D, A) = line.split()
        A = int(A)
        if D == 'forward':
            h += A
            d += a * A
        if D == 'up':
            a -= A
        if D == 'down':
            a += A
    print(str(h) + " " + str(d))
    return h * d

output = open('output', 'w')
output.write(str(simple(I))+'\n'+str(aim(I))+'\n')
output.close()