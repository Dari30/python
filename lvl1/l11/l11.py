grid = [["table", "chair", "wardrobe"],
        ["chair", "      ", "armchair"]]


def print_area():
    for row in grid:
        print(row)


def object(txt):
    while True:
        row = int(input(f"Enter row number {txt}:  ")) - 1
        if 0<=r<=1:
            break
    column = int(input(f"Enter column number {txt}: ")) - 1
    return row, column


def diagonal(r, c, rt, ct)
    if rt == r - 1 and ct == c - 1
        return True


while True:
    print_area()
    while True:
        while True:
            r, c = object("of thr object you want to move")
            if grid[r][c] != "      ":
                break
        while True:
            rt, ct = object("of the cell where you want to move")
            if grid[rt][ct] == "      ":
                break
        if not diagonal(r,c,rt,ct):
            break
    grid[r][c], grid[rt][ct] = grid[rt][ct], grid[r][c]
    if "wardrobe" == grid[1][2] and "armchair" == grid[0][2]:
        print("You have won")
        break
