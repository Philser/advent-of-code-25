import re
from dataclasses import dataclass


@dataclass
class Problem:
    operand: str
    numbers: list[int]


@dataclass
class ProblemChall2:
    operand: str
    numbers: list[int]


def parse_input(filename: str) -> list[Problem]:
    problems = []
    with open(filename) as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line_numbers = lines[i].split()
            for j in range(0, len(line_numbers)):
                num = line_numbers[j]
                if i == 0:
                    problems.append(Problem(numbers=[int(num)], operand=""))
                elif i == len(lines) - 1:
                    problems[j].operand = num
                else:
                    problems[j].numbers.append(int(num))

    return problems


def calc(op: str, left: int, right: int) -> int:
    if op == "*":
        return left * right
    if op == "+":
        return left + right

    raise Exception("Unsupported operand " + op)


def challenge1(problems: list[Problem]):
    sum = 0
    intermediate: int = 0
    for problem in problems:
        intermediate = problem.numbers[0]
        for i in range(1, len(problem.numbers)):
            intermediate = calc(problem.operand, intermediate, problem.numbers[i])
        sum += intermediate

    return sum


def parse_input_chall2(filename: str) -> list[ProblemChall2]:
    problems = []
    with open(filename) as f:
        lines = f.readlines()
        lines = lines[:len(lines)]
        problem = ProblemChall2(operand="", numbers=[])
        for col in range(0, len(lines[0])):
            vertical = ""
            for l in range(0, len(lines)):
                if l == len(lines) - 1:
                    if lines[l][col] == "*" or lines[l][col] == "+":
                        problem.operand = lines[l][col]
                else:
                    vertical += lines[l][col]
            if vertical.replace(" ", "").replace("\n", "") == "":
                problems.append(problem)
                problem = ProblemChall2(operand="", numbers=[])
                continue
            problem.numbers.append(int(vertical))

    return problems



def challenge2(problems: list[ProblemChall2]) -> int:
    sum = 0
    for problem in problems:
        intermediate = problem.numbers[0]
        for i in range(1, len(problem.numbers)):
            next = problem.numbers[i]
            intermediate = calc(
                problem.operand,
                intermediate,
                next
            )

        sum += intermediate

    return sum


def main():
    parsed = parse_input("day6/input.txt")
    result = challenge1(parsed)
    print(f"Solution to challenge 1: {result}")
    parsed = parse_input_chall2("day6/input.txt")
    result = challenge2(parsed)
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()
