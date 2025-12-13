def parse_input(filename) -> list[list[int]]:
    with open(filename) as f:
        content  = f.readlines()
        battery_banks = []
        for i in range(0, len(content)):
            battery_banks.append([])
            for j in range(0, len(content[i]) - 1 ): # skip over \n
                battery_banks[i].append(int(content[i][j]))

        return battery_banks


def challenge1(battery_banks: list[list[int]]):
    total_sum = 0
    for bank in battery_banks:
        max_ten = 1
        max_ten_pos = 0
        max_one = 1
        for pos in range(0, len(bank) - 1):
            if bank[pos] > max_ten:
                max_ten = bank[pos]
                max_ten_pos = pos
                if max_ten == 9:
                    break

        for pos in range(max_ten_pos + 1, len(bank)):
            if bank[pos] > max_one:
                max_one = bank[pos]
                if max_one == 9:
                    break

        total_sum += 10 * max_ten + max_one

    return total_sum

def challenge2(battery_banks: list[list[int]]):
    total_sum = 0
    for bank in battery_banks:
        max_leading_no = 1
        max_leading_no_pos = 0
        for pos in range(0, len(bank) - 11):
            if bank[pos] > max_leading_no:
                max_leading_no = bank[pos]
                max_leading_no_pos = pos
                if max_leading_no == 9:
                    break

        max_no_pos = max_leading_no_pos
        numbers = []
        max_no = 1
        for i in range(0, 11):
            max_no = 1
            for j in range(max_no_pos + 1, len(bank) - 10 + i):
                if bank[j] > max_no:
                    max_no = bank[j]
                    max_no_pos = j
                    if max_no == 9:
                        break

            numbers.append(max_no)

        total_sum += int(f"{max_leading_no}{''.join(map(str, numbers))}")

    return total_sum


def main():
    battery_banks = parse_input("input.txt")
    result = challenge1(battery_banks)
    print(f"Solution to challenge 1: {result}")
    result = challenge2(battery_banks)
    print(f"Solution to challenge 2: {result}")

if __name__ == "__main__":
    main()
