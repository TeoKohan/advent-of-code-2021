# target area: x=48..70, y=-189..-148

def step(px, py, vx, vy):
    px += vx
    py += vy
    if vx != 0:
        vx = vx - 1 if vx > 0 else vx + 1
    vy -= 1
    return px, py, vx, vy

H = []
Q = 0

for vx, vy in [(vx, vy) for vx in range(71) for vy in range(-189, 189)]:
    px, py = 0, 0
    ox, oy = vx, vy
    hy = 0
    while px < 70 and py > -189:
        px, py, vx, vy = step(px, py, vx, vy)
        hy = max(hy, py)
        if 48 <= px <= 70 and -189 <= py <= -148:
            Q += 1
            H += [hy]
            break

output = open('output', 'w')
output.write(str(max(H))+'\n'+ str(Q) +'\n')
output.close()