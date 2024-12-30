from utils.input import get_input

def main():
    input = get_input(2015, 3)
    santa_position = (0, 0)
    robo_santa_position = (0, 0)
    visited = set()
    for i, direction in enumerate(input):
        if i % 2 == 0:
            match direction:
                case "^":
                    santa_position = (santa_position[0], santa_position[1] + 1)
                case "v":
                    santa_position = (santa_position[0], santa_position[1] - 1)
                case ">":
                    santa_position = (santa_position[0] + 1, santa_position[1])
                case "<":
                    santa_position = (santa_position[0] - 1, santa_position[1])
            visited.add(santa_position)
        else:
            match direction:
                case "^":
                    robo_santa_position = (robo_santa_position[0], robo_santa_position[1] + 1)
                case "v":
                    robo_santa_position = (robo_santa_position[0], robo_santa_position[1] - 1)
                case ">":
                    robo_santa_position = (robo_santa_position[0] + 1, robo_santa_position[1])
                case "<":
                    robo_santa_position = (robo_santa_position[0] - 1, robo_santa_position[1])
            visited.add(robo_santa_position)
    answer = len(visited)
    print(f"2015 Day 3 Part 2: {answer}")

if __name__ == "__main__":
    main()