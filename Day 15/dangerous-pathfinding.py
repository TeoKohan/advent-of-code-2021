from math import inf

I = [line.strip() for line in open('input')]
I = [[int(n) for n in line] for line in I]

def dijkstra (grid):
    distances = [[inf for cell in row] for row in grid]
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
    S = { }
    S[0, 0] = 0
    distances[0][0] = grid[0][0]
 
    while len(S) > 0:
        x, y = min(S, key = lambda k: S[k])
        del S[x, y]
 
        for u, v in [(x+u, y+v) for u, v in D if 0 <= x+u < len(grid[0]) and 0 <= y+v < len(grid)]:
            if distances[u][v] > distances[x][y] + grid[u][v]:
                S[u, v] = distances[u][v] = distances[x][y] + grid[u][v]

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