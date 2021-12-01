import sys
import os


dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

forest = []

with open(file_path, "r") as input_file:
    for entry in input_file:
        forest.append([char for char in entry])

print(forest)