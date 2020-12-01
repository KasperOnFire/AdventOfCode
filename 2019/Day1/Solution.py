import sys
import os
import math


dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

list_of_module_masses = []

with open(file_path, "r") as input_file:
    for line in input_file:
        list_of_module_masses.append(int(line.strip()))

total_needed_fuel = sum(
    [math.floor(module_mass/3)-2 for module_mass in module_masses])
print(total_needed_fuel)
