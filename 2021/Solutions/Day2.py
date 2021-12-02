from pathlib import Path


def calculate_route_and_return_product(inputs: list[(str, int)]) -> int:
    current_depth = 0
    current_horizontal = 0
    for command in inputs:
        match command[0]:
            case "down":
                current_depth += command[1]
            case "up":
                current_depth -= command[1]
            case "forward":
                current_horizontal += command[1]
    return current_depth * current_horizontal


def calculate_route_with_aim_and_return_product(inputs: list[(str, int)]) -> int:
    current_depth = 0
    current_horizontal = 0
    current_aim = 0
    for command in inputs:
        match command[0]:
            case "down":
                current_aim += command[1]
            case "up":
                current_aim -= command[1]
            case "forward":
                current_horizontal += command[1]
                current_depth += command[1] * current_aim
    return current_depth * current_horizontal


if __name__ == '__main__':
    with open(Path("../Data/Day2Input.txt"), 'r') as f:
        data = [x for x in f.read().splitlines()]
        route = []
        for line in data:
            data = line.split()
            data = [data[0], int(data[1])]
            cmd = tuple(data)
            route.append(cmd)
    print(calculate_route_and_return_product(route))
    print(calculate_route_with_aim_and_return_product(route))
