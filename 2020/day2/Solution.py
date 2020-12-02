import sys
import os


dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

entries = []

with open(file_path, "r") as input_file:
    for line in input_file:
        entries.append(line.strip())

# part 1
valid_pw_count = 0
for line in entries:    
    chars_range, char, pw = line.split(" ")
    min_chars = chars_range.split("-")[0]
    max_chars = chars_range.split("-")[1]
    char=char[0]
    if pw.count(char) >= min_chars and pw.count(char) <= max_chars:
        valid_pw_count +=!

