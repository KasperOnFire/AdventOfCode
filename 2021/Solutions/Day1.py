from os import read
from pathlib import Path

input_file = Path("../Data/Day1Input.txt")

sonar_readings = []

with open(input_file) as inputs:
    for i in inputs:
        sonar_readings.append(int(i))

def part_1(sonar_readings: list) -> int:
    incr = 0
    for i, reading in enumerate(sonar_readings):
        if reading > sonar_readings[i-1]:
            incr += 1
    return incr

print(part_1(sonar_readings))

def part_2(sonar_readings: list) -> int:
    incr = 0
    last = 0
    for i in range(len(sonar_readings)-2):
        window = sum(sonar_readings[i:i+3])
        if i > 0 and window > last:
            incr += 1
        last = window
    return incr

print(part_2(sonar_readings))