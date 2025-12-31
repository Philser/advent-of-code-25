#!/bin/bash

DIRNAME=$1
if [ -d "$DIRNAME" ]; then
    echo "Directory $1 already exists. Exiting..."
    exit 0
fi

mkdir -p "$DIRNAME"

touch "$DIRNAME/input.txt"
touch "$DIRNAME/example.txt"
touch "$DIRNAME/$DIRNAME.py"

echo "import sys

def parse_input(filename: str):
    with open(filename) as f:
        # TODO
        return

def challenge1(input):
    pass

def challenge2(input):
    pass

def main():
    parsed = parse_input(sys.argv[1])
    result = challenge1(parsed)
    print(f'Solution to challenge 1: {result}')
    result = challenge2(parsed)
    print(f'Solution to challenge 2: {result}')

if __name__ == '__main__':
    main()

" >> "$DIRNAME/$DIRNAME.py"
