def read_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        if content[-1] == "\n":
            content.pop()
        return content

def chall1(content):
    content = read_file("./input.txt")

    pos = 50
    zeroes = 0
    for instruction in content:
        direction = instruction[0]
        if direction == "L":
            amount = -int(instruction[1:])
        elif direction == "R":
            amount = int(instruction[1:])
        else:
            raise Exception(f"Malformed instruction: {instruction}")

        pos = (pos + amount) % 100

        if pos == 0:
            zeroes += 1

    return zeroes

def chall2(content):
    pos = 50
    zeroes = 0
    for instruction in content:
        direction = instruction[0]
        amount = int(instruction[1:])
        divisible_by_hundred = int(amount / 100)

        zeroes += divisible_by_hundred # passing the 0 and ending up where we started
        amount -= 100 * divisible_by_hundred

        if direction == "L":
            if pos != 0:
                discr = amount - pos
                if discr > 0:
                    zeroes += 1
            pos  = (pos - amount) % 100
        elif direction == "R":
            if pos != 0:
                discr = pos + amount
                if discr > 100:
                    zeroes += 1
            pos = (pos + amount) % 100
        else:
            raise Exception(f"Malformed instruction: {instruction}")

        if pos == 0:
            zeroes += 1
    return zeroes

if __name__ == "__main__":
    content = read_file("./input.txt")
    print(f"Challenge 1: The secret code is {chall1(content)}")
    print(f"Challenge 2: The secret code is {chall2(content)}")
