def calculate_route_and_return_product(data: List[(str, int)]) -> int:
    current_depth = 0
    current_horizontal = 0
    for command in data:
        match command[0]:
            case "down":
                current_depth += command[1]
            case "up":
                current_depth -= command[1]
            case "forward":
                current_horizontal += command[1]
    return current_depth * current_horizontal

if __name__ == '__main__':
    with open('../Data/Day2Input.txt', 'r') as f:
        data = [x for x in f.read().splitlines()]
        route = []
        for line in data:
            cmd = tuple(str(x[0]), int(x[1]) for x in line.split())
            route.append(cmd)

    print(calculate_route_and_return_product(route))