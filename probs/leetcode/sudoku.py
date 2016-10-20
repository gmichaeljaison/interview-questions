import sys

grid = []
std = {1, 2, 3, 4, 5, 6, 7, 8, 9}
zeros = []
with open('../../input/sudoku.txt', 'r') as f:
    for line in f:
        stringList = line.split(',')
    for i, string in enumerate(stringList):
        row = [0] * 9
        for j, char in enumerate(string):
            print(char)
            if stringList[i][j] == '.':
                row[j] = 0
            else:
                row[j] = int(stringList[i][j])
        grid.append(row)
# grid[i][j] = 0 if stringList[i][j] == ‘.’ else int(stringList[i][j])
print(grid)


def isValid(grid):
    valid = False
    for i, row in enumerate(grid):
        if set(row) == std and set([grid[i][col] for col in range(len(grid))]) == std:
            valid = True
        else:
            valid = False
            break
    return valid


def sudoku(grid):
    if isValid(grid):
        return True

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                allowedSet = std.difference(row)
                allowedSet = allowedSet.difference([grid[i][col] for col in range(len(grid))])
                starti = (i // 3) * 3
                startj = (j // 3) * 3
                allowedSet = allowedSet.difference(
                    [grid[a][b] for a in range(starti, starti + 3, 1) for b in range(startj, startj + 3, 1)])
                if allowedSet:
                    for element in allowedSet:
                        grid[i][j] = element
                        solved = sudoku(grid)
                        if solved:
                            return solved
                else:
                    return False


sudoku(grid)
print(grid)