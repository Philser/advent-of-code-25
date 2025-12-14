def parse_input(filename) -> list[str]:
    with open(filename) as f:
        grid = []
        lines = f.readlines()
        for line in lines:
            grid.append(line[0:-1])

        return grid

def challenge1(grid: list[str]):
    accessible_rolls = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] != '@':
                continue
            rolls = count_neighbours(grid, x, y)
            if rolls < 4:
                accessible_rolls += 1

    return accessible_rolls

def count_neighbours(grid: list[str], x: int, y: int):
    neighbours = 0
    probe_y = [y]
    if y > 0:
        probe_y.append(y-1)
    if y < len(grid) - 1:
        probe_y.append(y+1)
    probe_x = [x]
    if x > 0:
        probe_x.append(x-1)
    if x < len(grid[y]) - 1:
        probe_x.append(x+1)

    for pry in probe_y:
        for prx in probe_x:
            if pry == y and prx == x:
                continue
            if grid[pry][prx] == '@':
                neighbours += 1

    return neighbours

def challenge2(grid: list[str]):
    total_accessible_rolls = 0
    accessible_rolls = -1
    rolls_to_remove = []
    while accessible_rolls != 0:
        accessible_rolls = 0
        if len(rolls_to_remove):
            for coords in rolls_to_remove:
                grid[coords[1]] = grid[coords[1]][:coords[0]] + "." + grid[coords[1]][coords[0] + 1:]
            rolls_to_remove = []
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] != '@':
                    continue
                rolls = count_neighbours(grid, x, y)
                if rolls < 4:
                    total_accessible_rolls += 1
                    accessible_rolls += 1
                    rolls_to_remove.append([x, y])

    return total_accessible_rolls


def main():
    grid = parse_input('input.txt')
    result = challenge1(grid)
    print(f"Solution to challenge 1: {result}")
    result = challenge2(grid)
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()