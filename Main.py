grid = []                                                       # Setting grid to an empty array

# Creates a grid using the contents of a text file
def get_grid():
    f = open('test_grid.txt', 'r')                              # Open a file called 'test_grid.txt' and read it
    for x in f:                                                 # For every line in f
        arr = [int(i) for i in x.rstrip('\n').split(',')]       # Separates the numbers by ',' and converts them to integers
        grid.append(arr)                                        # Add that simplified array to the grid

# Finds the empty space (0) within the grid
def empty_space(g):
    for index_one, i in enumerate(g):                           # For every array in list g
        for index_two, j in enumerate(i):                       # For every number in array i
            if g[index_one][index_two] == 0:                    # If the number at indexes index_one and index_two is equal to 0
                return index_one, index_two                     # Return index_one (row) and index_two (column)
    return None                                                 # If it makes it through these loops, return None

# Check to see if the given position and number is valid
def valid_pos(g, pos, num):
    # Checks row
    for index, i in enumerate(g):                               # For every array in list g
        if g[pos[0]][index] == num and pos[0] != i:             # If the number at indexes pos[0] and index are equal to the given number and row does not equal i
            return False                                        # Then return false

    # Checks column
    for index, i in enumerate(g):                               # For every array in list g
        if g[index][pos[1]] == num and pos[1] != i:             # If the number at indexes pos[1] and index are equal to the given number and col does not equal i
            return False                                        # Then return false

    # Checks square
    row = pos[0] // 3                                           # Divide pos[0] by three and round down
    col = pos[1] // 3                                           # Divide pos[1] by three and round down

    if row == 0 and col == 0:                                   # If the desired position is at row = 0 and col = 0
        for i in range(3):
            if g[0][i] == num and pos[1] != i:                  # If the number in square 0 at index is equal to num and col is not equal to i
                return False                                    # Then return false
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

    return True                                                 # If it makes it through all that, then the conditions must be true

# Prints out the grid
def print_grid(g):
    for count_one, i in enumerate(g):                               # For every array in list g
        for count_two, j in enumerate(i):                           # For every number in array i
            if count_two % 3 == 0 and count_two != 0:               # If the remainder of count_two / 3 is equal to zero and count_two does not equal zero
                print("|  ", end="")                                # Print a vertical pipe character
            print(j, end="")                                        # Print the number
            print("  ", end="")                                     # Separate the numbers
        print()                                                     # Print a new line
        if (count_one + 1) % 3 == 0 and count_one + 1 != len(g):    # If the remainder of count_one+1 / 3 is equal to zero and count_one+1 does not equal the length of g
            print("-  -  -  -  -  -  -  -  -  -  -")                # Print a separator

# Solves the puzzle recursively
def solve(g):
    empty = empty_space(g)      # Call the empty_space function and set the return value of it equal to empty
    if not empty:               # If empty has nothing in it
        return True             # Then the puzzle is solved
    else:
        row, col = empty        # Set row and col equal to empty

    for i in range(1, 10):
        if valid_pos(g, [row, col], i):     # If the function valid_pos returns true
            g[row][col] = i                 # Then set g at the index of row, col equal to i
            if solve(g):                    # Call the recursive function and if it returns true
                return True                 # Then return true
            g[row][col] = 0                 # Else, backtrack by setting g at the index of row, col equal to 0


get_grid()
print_grid(grid)
solve(grid)
print()
print()
print_grid(grid)
