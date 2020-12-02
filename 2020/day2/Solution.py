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
    min_chars = int(chars_range.split("-")[0])
    max_chars = int(chars_range.split("-")[1])
    char=char[0]
    if pw.count(char) >= min_chars and pw.count(char) <= max_chars:
        valid_pw_count +=1

        
print(valid_pw_count)

#part 2
valid_pw_count_2 = 0
for line in entries:    
    chars_range, char, pw = line.split(" ")
    pos_1 = int(chars_range.split("-")[0])-1
    pos_2 = int(chars_range.split("-")[1])-1
    char=char[0]
    if pw[pos_1] == char and pw[pos_2] == char:
        continue
    elif pw[pos_1] == char or pw[pos_2] == char:
        valid_pw_count_2 +=1

print(valid_pw_count_2)