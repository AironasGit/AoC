from utils.input import get_input
import re

def main():
    input = get_input(2015, 5)
    answer = 0
    for string in input.split("\n"):
        pairs = [string[i:i+2] for i in range(len(string) - 1)]
        if any([True for pair in pairs if string.count(pair) > 1]):
            if any([True for i in range(len(string) - 2) if string[i] == string[i+2]]):
                answer += 1
    print(f"2015 Day 5 Part 2: {answer}")

if __name__ == "__main__":
    main()