sequence = input()
sequence = list(sequence)

row1 = []
row2 = []

grid = [[0 for i in range(2)] for j in range(2)]
grid[0][0] = 1
grid[0][1] = 2
grid[1][0] = 3
grid[1][1] = 4

for i in range(len(sequence)):
    if sequence[i] == "H":
        topLeft = grid[0][0]
        topRight = grid[0][1]
        bottomLeft = grid[1][0]
        bottomRight = grid[1][1]
        grid[0][0] = bottomLeft
        grid[1][0] = topLeft
        grid[0][1] = bottomRight
        grid[1][1] = topRight
    elif sequence[i] == "V":
        topLeft = grid[0][0]
        topRight = grid[0][1]
        bottomLeft = grid[1][0]
        bottomRight = grid[1][1]
        grid[0][0] = topRight
        grid[0][1] = topLeft
        grid[1][0] = bottomRight
        grid[1][1] = bottomLeft

for i in range(2):
    row1.append(grid[0][i])
for i in range(2):
    row2.append(grid[1][i])

print(" ".join(str(i) for i in row1))
print(" ".join(str(i) for i in row2))
