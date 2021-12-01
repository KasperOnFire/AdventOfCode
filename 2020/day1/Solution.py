import sys
import os


dir_path = sys.path[0]
file_path = os.path.join(dir_path, "input.txt")

input_numbers = []

with open(file_path, "r") as input_file:
    for line in input_file:
        input_numbers.append(int(line.strip()))


def task_1(list_of_numbers):
    for a in list_of_numbers:
        for b in list_of_numbers:
            if a+b == 2020:
                print(a)
                print(b)
                return a*b
    raise Exception("No solution found!")


result_task_1 = task_1(input_numbers)
print("Result of task 1: " + str(result_task_1))


def task_2(list_of_numbers):
    for a in list_of_numbers:
        for b in list_of_numbers:
            for c in list_of_numbers:
                if a+b+c == 2020:
                    print(a)
                    print(b)
                    print(c)
                    return a*b*c
    raise Exception("No solution found!")


result_task_2 = task_2(input_numbers)
print("Result of task 2: " + str(result_task_2))
