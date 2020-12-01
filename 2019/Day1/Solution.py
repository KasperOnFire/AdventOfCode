import sys
import os

dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

list_of_module_masses = []

with open(file_path, "r") as input_file:
    for line in input_file:
        list_of_module_masses.append(int(line))


def calc_fuel(mass):
    fuel_needed = mass // 3 - 2
    if fuel_needed < 0:
        return 0
    else:
        return fuel_needed


# Part 1
part_1_fuel = sum([calc_fuel(module_mass) for module_mass in list_of_module_masses])
print(part_1_fuel)


# Part 2
def calc_fuel_recursive(mass):
    fuel_needed = mass // 3 - 2
    if fuel_needed <= 0:
        return 0
    else:
        return fuel_needed + calc_fuel_recursive(fuel_needed)


total_fuel_needed_recursive = sum([calc_fuel_recursive(element) for element in list_of_module_masses])
print(total_fuel_needed_recursive)