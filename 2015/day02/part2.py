from utils.input import get_input

def main():
    input = get_input(2015, 2)
    answer = 0
    for dimentions in input.split("\n"):
        length, width, height = list(map(int, dimentions.split("x")))
        answer += 2*min(length + width, length + height, width + height) + length*width*height
    print(f"2015 Day 2 Part 2: {answer}")

if __name__ == "__main__":
    main()