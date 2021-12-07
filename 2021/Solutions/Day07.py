import statistics as stats
from pathlib import Path


def part_1(x_positions: list[int]) -> int:
    median = int(stats.median(x_positions))
    total_fuel_cost = sum([abs(x - median) for x in x_positions])
    # for pos in x_positions:
    #    total_fuel_cost += median - pos if pos < median else pos - median
    return total_fuel_cost


def part_2(x_positions: list[int]) -> int:
    min_pos, max_pos = min(x_positions), max(x_positions)
    position_range = max_pos - min_pos
    # To not divide by zero in cost calculation we add 0 as a starting value
    cost_per_step = [0]
    # We skip 0 steps, as it is always free
    for idx in range(1, position_range + 1):
        # calculate nth triangle number
        cost = (idx ** 2 + idx) // 2
        cost_per_step.append(cost)

    costs = []
    for x in x_positions:
        steps = [abs(x - step) for step in range(position_range + 1)]
        pos_costs = [cost_per_step[x] for x in steps]
        costs.append(pos_costs)
    fuel_costs = [sum(x) for x in zip(*costs)]
    return min(fuel_costs)


def run_test():
    test_val = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    print("Test Runs")
    print(part_1(test_val))
    print(part_2(test_val))


run_test()

with open(Path("../Data/Day07Input.txt"), 'r') as f:
    print("Actual Runs")
    data = [int(x) for x in f.read().split(",")]
    print(part_1(data))
    print(part_2(data))
