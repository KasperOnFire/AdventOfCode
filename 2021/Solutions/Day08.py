import statistics as stats
from pathlib import Path


def part_1(circuit_input: list[tuple(str, str)]) -> int:
    pass


def part_2(circuit_input: list[tuple(str, str)]) -> int:
    pass


def run_test():
    test_val = [("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab","cdfeb fcadb cdfeb cdbaf")]
    print("Test Runs")
    print(part_1(test_val))
    print(part_2(test_val))


run_test()

with open(Path("../Data/Day08Input.txt"), 'r') as f:
    print("Actual Runs")
    data = [str(x) for x in f.read().split(",")]
    print(part_1(data))
    print(part_2(data))
