from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Vertex:
    id: int
    x: int
    y: int


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
            diagram[y + 1][x - 1] = "|"
            diagram[y + 1][x + 1] = "|"

    if output_file is not None:
        final = []
        for line in diagram:
            final.append("".join(line))
        with open(output_file, "w") as f:
            f.write("".join(final))

    return split_count


def challenge2(diagram: list[list[str]]):
    # count the number of possible paths to get to a beam
    # at the end, add them all together
    # I couldnt do the challenge myself so took inspiration from 0xdf's YT channel
    # https://www.youtube.com/watch?v=sq2OdJY3D_4&list=PLJt6nPUdQbiRZnP5UJY2bvi6OSSt62qT7&index=8
    beams = defaultdict(int)
    for pos in range(0, len(diagram[0])):
        if diagram[0][pos] == "S":
            beams[pos] = 1
            break

    for y in range(2, len(diagram)):
        new_beams = defaultdict(int)
        for x in beams:
            if diagram[y][x] == "|" or diagram[y][x] == ".":
                new_beams[x] += beams[x]
            if diagram[y][x] == "^":
                new_beams[x - 1] += beams[x]
                new_beams[x + 1] += beams[x]

        beams = new_beams

    return sum(beams.values())


def main():
    parsed = parse_input("day7/input.txt")
    result = challenge1(parsed, "day7/output.txt")
    print(f"Solution to challenge 1: {result}")
    result = challenge2(parsed)
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()
