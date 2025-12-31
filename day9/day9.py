import sys
from collections import defaultdict


def parse_input(filename: str) -> list[list[int]]:
    with open(filename) as f:
        lines = f.readlines()
        return list(map(lambda line: list(map(int, line[:-1].split(","))), lines))


def challenge1(grid: list[list[int]]):
    max_rect_area = 0
    for i in range(0, len(grid)):
        x1, y1 = grid[i]
        for j in range(i + 1, len(grid)):
            x2, y2 = grid[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_rect_area:
                max_rect_area = area

    return max_rect_area


def chall2_rect_is_elligible_2(
    grid: list[list[str]], coords1: list, coords2: list
) -> bool:
    x1, y1 = coords1
    x2, y2 = coords2
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if grid[y][x] != "X" and grid[y][x] != "#":
                return False
    return True


def challenge2(red_coords: list[list[int]]):
    # TODO: SLOOOOOOW :(
    # Apparently you could use a technique called ray finding but right now I cannot be bothered

    # find greens connecting reds
    greens = defaultdict(set)
    reds = defaultdict(set)
    prev_x, prev_y = red_coords[0]
    reds[prev_y].add(prev_x)
    for i in range(1, len(red_coords) + 1):
        if i == len(red_coords):
            prev_x, prev_y = red_coords[0]
            x, y = red_coords[i - 1]
        else:
            x, y = red_coords[i]
        reds[y].add(x)
        if x == prev_x:
            for green_y in range(min(prev_y, y) + 1, max(prev_y, y)):
                greens[green_y].add(x)
        else:
            for green_x in range(min(prev_x, x) + 1, max(prev_x, x)):
                greens[y].add(green_x)
        prev_x = x
        prev_y = y

    # find the allowed x coords per y where a rectangle is allowed to exist
    enclosed_coords = {}
    for y in greens:
        sorted_greens = list(greens[y])
        sorted_greens.sort()
        min_x = sorted_greens[0]
        if y in reds:
            min_x = min(min_x, min(reds[y]))
        max_x = sorted_greens[-1]
        if y in reds:
            max_x = max(max_x, max(reds[y]))
        enclosed_coords[y] = [min_x, max_x]

    # find biggest rectangle
    max_rect_area = 0
    for i in range(0, len(red_coords)):
        x1, y1 = red_coords[i]
        for j in range(i + 1, len(red_coords)):
            x2, y2 = red_coords[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            if area > max_rect_area:
                is_elligible = True
                for y in range(min_y, max_y + 1):
                    x_left, x_right = enclosed_coords[y]
                    if x_left > min_x or x_right < max_x:
                        is_elligible = False
                        break
                if is_elligible:
                    max_rect_area = area

    return max_rect_area


def main():
    parsed = parse_input(sys.argv[1])
    result = challenge1(parsed)
    print(f"Solution to challenge 1: {result}")
    result = challenge2(parsed)
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()
