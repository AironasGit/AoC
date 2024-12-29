from utils.input import get_input

def main():
    input = get_input(2015, 2)
    answer = 0
    for dimentions in input.split("\n"):
        length, width, height = list(map(int, dimentions.split("x")))
        side1, side2, side3 = length*width, width*height, height*length
        answer += 2*(side1 + side2 + side3) + min(side1, side2, side3)
    print(f"2015 Day 2 Part 1: {answer}")

if __name__ == "__main__":
    main()