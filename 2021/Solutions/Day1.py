from pathlib import Path

input_file = Path("../Data/Day1Input.txt")

sonar_readings = []

with open(input_file) as inputs:
    for i in inputs:
        sonar_readings.append(int(i))


def part_1(input_readings: list) -> int:
    incr = 0
    for i, reading in enumerate(input_readings):
        if reading > input_readings[i - 1]:
            incr += 1
    return incr


print(part_1(sonar_readings))


def part_2(input_readings: list) -> int:
    incr = 0
    last = 0
    for i in range(len(input_readings) - 2):
        window = sum(input_readings[i:i + 3])
        if i > 0 and window > last:
            incr += 1
        last = window
    return incr


print(part_2(sonar_readings))
