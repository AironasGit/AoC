from utils.input import get_input
import hashlib

def main():
    input = get_input(2015, 4)
    answer = 0
    while True:
        if hashlib.md5(f"{input}{answer}".encode()).hexdigest().startswith("000000"):
            break
        answer += 1
    print(f"2015 Day 4 Part 2: {answer}")

if __name__ == "__main__":
    main()