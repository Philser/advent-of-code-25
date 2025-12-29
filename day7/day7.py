def parse_input(filename: str) -> list[list[str]]:
    lines = []
    with open(filename) as f:
        l = f.readlines()
        for line in l:
            chr_list = []
            for char in line:
                chr_list.append(char)
            lines.append(chr_list)

    return lines


def challenge1(diagram: list[list[str]], output_file=None):
    start_pos = 0
    split_count = 0
    for pos in range(0, len(diagram[0])):
        if diagram[0][pos] == "S":
            start_pos = pos
            break
    diagram[1][start_pos] = "|"

    for y in range(1, len(diagram) - 1):
        for x in range(0, len(diagram[y])):
            if diagram[y][x] != "|":
                continue

            if diagram[y + 1][x] != "^":
                diagram[y + 1][x] = "|"
                continue

            split_count += 1
            if x - 1 >= 0:
                diagram[y + 1][x - 1] = "|"
            if x + 1 <= len(diagram[y]) - 1:
                diagram[y + 1][x + 1] = "|"

    if output_file is not None:
        final = []
        for line in diagram:
            final.append("".join(line))
        with open(output_file, "w") as f:
            f.write("".join(final))

    return split_count


def challenge2(diagram: list[list[str]]):
    start_pos = 0
    split_count = 0
    for pos in range(0, len(diagram[0])):
        if diagram[0][pos] == "S":
            start_pos = pos
            break
    diagram[1][start_pos] = "|"

    stack = []
    for y in range(1, len(diagram) - 1):
        for x in range(0, len(diagram[y])):
            if diagram[y][x] != "|":
                continue

            if diagram[y + 1][x] != "^":
                diagram[y + 1][x] = "|"
                continue

            if x - 1 >= 0:
                stack.append({"pos": {'x': x, 'y': y}, "dir": "l"})
                diagram[y + 1][x - 1] = "|"
            if x + 1 <= len(diagram[y]) - 1:
                stack.append({"pos": {'x': x, 'y': y}, "dir": "r"})
                diagram[y + 1][x + 1] = "|"
    return


def main():
    parsed = parse_input("day7/input.txt")
    result = challenge1(parsed)
    print(f"Solution to challenge 1: {result}")
    parsed = parse_input("day7/input.txt")
    result = challenge2(parsed)
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()
