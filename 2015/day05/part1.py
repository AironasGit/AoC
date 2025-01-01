from utils.input import get_input
import re

def main():
    input = get_input(2015, 5)
    answer = 0
    for string in input.split("\n"):
        if len(re.findall(r'[aeiou]', string)) >= 3:
            if any([string[i] == string[i+1] for i in range(len(string) - 1)]):
                if not any([string.__contains__(substring) for substring in ["ab", "cd", "pq", "xy"]]):
                    answer += 1
    print(f"2015 Day 5 Part 1: {answer}")

if __name__ == "__main__":
    main()