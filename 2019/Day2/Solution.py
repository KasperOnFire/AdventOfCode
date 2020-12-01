import sys
import os

dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

spaceship_intcode = []

with open(file_path, "r") as input_file:
    for entry in input_file:
        for num in entry.split(","):
            spaceship_intcode.append(int(num))

# preparation
spaceship_intcode[1] = 12
spaceship_intcode[2] = 2

test_intcode = [1, 0, 0, 3, 99]
# modifies input object
def intcode_computer(intcode):
    output = [x for x in intcode]
    skip = 0
    for idx, cmd in enumerate(intcode):
        if skip > 0:
            print("skipping")
            skip -= 1
        else:
            print(f"current command: {cmd}")
            if cmd == 99:
                break
            elif cmd == 1:
                value_1 = intcode[intcode[idx + 1]]
                value_2 = intcode[intcode[idx + 2]]
                output_idx = intcode[intcode[idx + 3]]
                result = value_1 + value_2
                print(result)
                output[output_idx] = result
                print(output[output_idx])
                skip = 3
            elif cmd == 2:
                value_1 = intcode[intcode[idx + 1]]
                value_2 = intcode[intcode[idx + 2]]
                output_idx = intcode[intcode[idx + 3]]
                result = value_1 * value_2
                output[output_idx] = result
                skip = 3
            else:
                pass
    return output


res = intcode_computer(test_intcode)
print(res)
