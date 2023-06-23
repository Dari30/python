def winner(symbol):
    if grid[0][0] == symbol and grid[0][1] == symbol and grid[0][2] == symbol:
        return True
    elif grid[1][0] == symbol and grid[1][1] == symbol and grid[1][2] == symbol:
        return True
    elif grid[2][0] == symbol and grid[2][1] == symbol and grid[2][2] == symbol:
        return True
    elif grid[0][0] == symbol and grid[1][0] == symbol and grid[2][0] == symbol:
        return True
    elif grid[0][1] == symbol and grid[1][1] == symbol and grid[2][1] == symbol:
        return True
    elif grid[0][2] == symbol and grid[1][2] == symbol and grid[2][2] == symbol:
        return True
    elif grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    elif grid[2][0] == symbol and grid[1][1] == symbol and grid[0][2] == symbol:
        return True

def print_area():
    for row in grid:
        print(row)


grid = [["*", "*", "*"],
        ["*", "*", "*"],
        ["*", "*", "*"]]

turn = 0
while True:
    print_area()
    if turn % 2 == 0:
        symbol = "x"
    else:
        symbol = "o"
    print(f"It's {symbol}'s turn")
    row = int(input("Enter row number: "))
    row-=1
    column = int(input("Enter column number: "))-1
    if grid[row][column] != '*':
        continue
    grid[row][column] = symbol
    if winner("x"):
        print("x is winner")
        break
    elif winner("o"):
        print("o is winner")
        break
    elif turn == 8:
        print("draw")
        break
    turn += 1
