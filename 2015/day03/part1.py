from utils.input import get_input

def main():
    input = get_input(2015, 3)
    current_position = (0, 0)
    visited = set()
    for direction in input:
        match direction:
            case "^":
                current_position = (current_position[0], current_position[1] + 1)
            case "v":
                current_position = (current_position[0], current_position[1] - 1)
            case ">":
                current_position = (current_position[0] + 1, current_position[1])
            case "<":
                current_position = (current_position[0] - 1, current_position[1])
        visited.add(current_position)
    answer = len(visited)
    print(f"2015 Day 3 Part 1: {answer}")

if __name__ == "__main__":
    main()