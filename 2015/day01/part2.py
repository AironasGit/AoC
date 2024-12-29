from utils.input import get_input

def main():
    input = get_input(2015, 1)
    count = 0
    answer = 0
    for i, char in enumerate(input):
        count = count + 1 if char == "(" else count - 1 if char == ")" else count
        if count == -1:
            answer = i + 1
            break
    print(f"2015 Day 1 Part 2: {answer}")

if __name__ == "__main__":
    main()