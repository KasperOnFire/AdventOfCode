from pathlib import Path
from timeit import timeit


def part_1(fish_list: list[int], simulate_days: int) -> int:
    fishes = fish_list[:]
    # print(f"Simulating for {simulate_days} days")
    # print(f"Initial State: {fish_list}")
    for day in range(simulate_days):
        # print(f"After {day} days: {fishes}")
        # print(f"Simulating day {day}...")
        new_fish = []
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fishes[idx] = 6
                new_fish.append(8)
            else:
                fishes[idx] = fish - 1
        fishes = fishes + new_fish
    return len(fishes)


def part_2(fish_list: list[int], simulate_days: int) -> int:
    numbers = range(9)
    fish_freq = {}
    # Set start state
    for num in numbers:
        fish_freq[num] = 0
    for fish in fish_list:
        fish_freq[fish] += 1

    # Simulate evolution
    for day in range(simulate_days):
        # print(f"Simulating day {day+1}...")
        new_freq = dict(fish_freq)
        fish_to_reset = 0
        for val, count in fish_freq.items():
            match val:
                case 0:
                    new_freq[8] = count
                    fish_to_reset = count
                case _:
                    new_freq[val-1] = count
        new_freq[6] += fish_to_reset
        fish_freq = dict(new_freq)
    return sum(fish_freq.values())


def run_test():
    test_val = [3, 4, 3, 1, 2]
    print("TEST RUNS")
    print("Expected results:")
    print("26")
    print("5934")
    print("1732821262171")
    print("Actual Results:")
    print(part_1(test_val, 18))
    print(part_1(test_val, 80))
    print(part_2(test_val, 256))
    print("")

run_test()

with open(Path("../Data/Day06Input.txt"), 'r') as f:

    data = [int(x) for x in f.read().split(",")]
    days = 80
    print(part_1(data, days))
    days_2 = 256
    print(part_2(data, days_2))
