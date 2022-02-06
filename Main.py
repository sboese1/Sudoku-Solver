grid = []


def get_grid():
    f = open('test_grid.txt', 'r')
    for x in f:
        arr = [int(i) for i in x.rstrip('\n').split(',')]
        grid.append(arr)


def empty_space(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 0:
                return i, j  # row, col
    return None


def valid_pos(g, pos, num):
    for index, i in enumerate(g):
        if g[pos[0]][index] == num and pos[0] != i:
            return False

    for index, i in enumerate(g):
        if g[index][pos[1]] == num and pos[1] != i:
            return False

    row = pos[0] // 3
    col = pos[1] // 3

    if row == 0 and col == 0:
        for i in range(3):
            if g[0][i] == num and pos[1] != i:
                return False
            elif g[1][i] == num and pos[1] != i:
                return False
            elif g[2][i] == num and pos[1] != i:
                return False
    elif row == 0 and col == 1:
        for i in range(3, 6):
            if g[0][i] == num and pos[1] != i:
                return False
            elif g[1][i] == num and pos[1] != i:
                return False
            elif g[2][i] == num and pos[1] != i:
                return False
    elif row == 0 and col == 2:
        for i in range(6, 9):
            if g[0][i] == num and pos[1] != i:
                return False
            elif g[1][i] == num and pos[1] != i:
                return False
            elif g[2][i] == num and pos[1] != i:
                return False
    elif row == 1 and col == 0:
        for i in range(3):
            if g[3][i] == num and pos[1] != i:
                return False
            elif g[4][i] == num and pos[1] != i:
                return False
            elif g[5][i] == num and pos[1] != i:
                return False
    elif row == 1 and col == 1:
        for i in range(3, 6):
            if g[3][i] == num and pos[1] != i:
                return False
            elif g[4][i] == num and pos[1] != i:
                return False
            elif g[5][i] == num and pos[1] != i:
                return False
    elif row == 1 and col == 2:
        for i in range(6, 9):
            if g[3][i] == num and pos[1] != i:
                return False
            elif g[4][i] == num and pos[1] != i:
                return False
            elif g[5][i] == num and pos[1] != i:
                return False
    elif row == 2 and col == 0:
        for i in range(3):
            if g[6][i] == num and pos[1] != i:
                return False
            elif g[7][i] == num and pos[1] != i:
                return False
            elif g[8][i] == num and pos[1] != i:
                return False
    elif row == 2 and col == 1:
        for i in range(3, 6):
            if g[6][i] == num and pos[1] != i:
                return False
            elif g[7][i] == num and pos[1] != i:
                return False
            elif g[8][i] == num and pos[1] != i:
                return False
    elif row == 2 and col == 2:
        for i in range(6, 9):
            if g[6][i] == num and pos[1] != i:
                return False
            elif g[7][i] == num and pos[1] != i:
                return False
            elif g[8][i] == num and pos[1] != i:
                return False

    return True


def print_grid(g):
    for count_one, i in enumerate(g):
        for count_two, j in enumerate(i):
            if count_two % 3 == 0 and count_two != 0:
                print("|  ", end="")
            print(j, end="")
            print("  ", end="")
        print()
        if (count_one + 1) % 3 == 0 and count_one + 1 != len(g):
            print("-  -  -  -  -  -  -  -  -  -  -")


def solve(g):
    empty = empty_space(g)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if valid_pos(g, [row, col], i):
            g[row][col] = i
            if solve(g):
                return True
            g[row][col] = 0


get_grid()
print_grid(grid)
solve(grid)
print()
print()
print_grid(grid)
