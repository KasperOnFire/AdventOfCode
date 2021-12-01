import sys
import os


dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

input_numbers = []

with open(file_path, "r") as input_file:
    for entry in input_file:
        for num in entry.split(","):
            input_numbers.append(int(num))

count_blocks = 0
for idx, x in enumerate(input_numbers):
    if idx % 3 == 0 and x == 2:
        count_blocks +=1

print(count_blocks)