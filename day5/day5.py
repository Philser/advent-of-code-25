from dataclasses import dataclass


@dataclass
class IDRange:
    start: int
    end: int


def parse_input(filename: str):
    id_ranges = []
    ids = []
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            line = line.replace("\n", "")
            if "-" in line:
                range = line.split("-")
                id_ranges.append(IDRange(start=int(range[0]), end=int(range[1])))
            elif len(line) == 0:
                continue
            else:
                ids.append(int(line.replace("\n", "")))

    return [id_ranges, ids]


def challenge1(id_ranges, ids):
    fresh = 0
    for id in ids:
        for range in id_ranges:
            if id <= range.end and id >= range.start:
                fresh += 1
                break

    return fresh


def challenge2(id_ranges: list[IDRange]):
    sorted = id_ranges
    sorted.sort(key=lambda range: range.start)
    ids = 0
    stop = 0
    for id_range in sorted:
        if stop > id_range.end:
            continue

        if stop == id_range.start:
            ids += id_range.end - id_range.start
        elif stop > id_range.start:
            ids += id_range.end - stop
        else:
            ids += id_range.end - id_range.start + 1

        stop = id_range.end

    return ids


def main():
    parsed = parse_input("input.txt")
    result = challenge1(parsed[0], parsed[1])
    print(f"Solution to challenge 1: {result}")
    result = challenge2(parsed[0])
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()
