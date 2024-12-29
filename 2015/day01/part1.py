from utils.input import get_input

def main():
    input = get_input(2015, 1)
    answer = sum(1 if char == "(" else -1 if char == ")" else 0 for char in input)
    print(f"2015 Day 1 Part 1: {answer}")

if __name__ == "__main__":
    main()