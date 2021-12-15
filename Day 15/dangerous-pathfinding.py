from math import inf

I = [line.strip() for line in open('input')]
I = [[int(n) for n in line] for line in I]

def dijkstra(grid):
    distances = [[inf for cell in row] for row in grid]

    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
    S = set()
    S.add((0, 0, 0))

    distances[0][0] = grid[0][0]
 
    while (len(S) > 0):
        x, y, d = min(S, key = lambda x: x[2])
        S.remove((x, y, d))
 
        for u, v in D:
            if not (0 <= x+u < len(grid)) or not (0 <= y+v < len(grid)):
                continue

            if distances[x+u][y+v] > distances[x][y] + grid[x+u][y+v]:
                if distances[x+u][y+v] != inf:
                    S.remove((x, y, distances[x+u][y+v]))
                distances[x+u][y+v] = distances[x][y] + grid[x+u][y+v]

                S.add((x+u, y+v, distances[x+u][y+v]))

    return distances[-1][-1] - grid[0][0]

small_cave = dijkstra(I)

def increase_matrix(A, s):
    return [[n+s if n+s < 10 else ((n+s) % 10) + 1 for n in line] for line in A]

R = [line[:] for line in I]
for i in range(1, 5):
    R = [R[j]+increase_matrix(I, i)[j] for j in range(len(R))]
F = [line[:] for line in R]
for i in range(1, 5):
    F = F + increase_matrix(R, i)

big_cave = dijkstra(F)


output = open('output', 'w')
output.write(str(small_cave)+'\n'+ str(big_cave) +'\n')
output.close()