import math
from dataclasses import dataclass


@dataclass
class Range():
    start:int
    end: int

def parse_id_ranges(file_path) -> list[Range]:
    with open(file_path) as f:
        return list(map(lambda range : Range(start=int(range.split("-")[0]), end=int(range.split("-")[1])),
                     f.read().split(",")))

def challenge1(id_ranges: list[Range]):
    sum = 0
    for id_range in id_ranges:
        for id in range(id_range.start, id_range.end):
            stringified = str(id)
            str_len = len(stringified)
            if (str_len % 2 != 0):
                continue
            if stringified[0:int(str_len/2)] == stringified[int(str_len/2):str_len]:
                sum += id
                # print(f"Found eligible number {id}")
    return sum

def challenge2(id_ranges: list[Range]):
    sum = 0
    for id_range in id_ranges:
        for id in range(id_range.start, id_range.end):
            if is_repeating_sequence(id):
                sum += id
                # print(f"Found eligible number {id}")
    return sum

def find_divisors(number):
    divisors = [1]
    for i in range(2, number): # TODO: Boo, lazy! Make this more performant!
        if number % i == 0:
            divisors.append(i)


    divisors.sort(reverse=True)
    return divisors

def is_repeating_sequence(number: int):
    stringified = str(number)
    str_len = len(stringified)
    divisors = find_divisors(str_len)
    for div in divisors:
        parts = int(str_len / div)
        for i in range(0, parts):
            if stringified[div * i:div * i + div] != stringified[div * (i + 1):div * (i + 1) + div]:
                break
            if i == parts - 2:
                return True

    return False


def main():
    ranges = parse_id_ranges("./input.txt")
    result = challenge1(ranges)
    print(f"Solution to challenge 1: {result}")
    result = challenge2(ranges)
    print(f"Solution to challenge 2: {result}")

if __name__ == "__main__":
    main()