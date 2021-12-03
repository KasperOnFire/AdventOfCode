from pathlib import Path


def calculate_gamma_and_epsilon(inputs: list[str]) -> int:
    threshold = len(inputs)/2
    counts = [0] * len(inputs[0])
    
    for bit in inputs:
        for pos, i in enumerate(bit):
            if i == str(1):
                counts[pos] += 1

    gamma_binary = ""
    epsilon_binary = ""

    for i in counts:
        if i > threshold:
            gamma_binary += "1"
            epsilon_binary += "0"
        elif i < threshold:
            gamma_binary += "0"
            epsilon_binary += "1"
    
    gamma_decimal = int(gamma_binary, 2)
    epsilon_decimal = int(epsilon_binary, 2)
    return gamma_decimal * epsilon_decimal


def verify_life_support_rating(inputs: list[str]) -> int:
    oxygen_generator_rating = 0
    co2_scrupper_rating = 0
    counts = [0] * len(inputs[0])
    for bit in inputs:
        for pos, i in enumerate(bit):


            
if __name__ == '__main__':
    with open(Path("../Data/Day3Input.txt"), 'r') as f:
        data = [x for x in f.read().splitlines()]
        test = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

        print(calculate_gamma_and_epsilon(test))
        print(calculate_gamma_and_epsilon(data))

        print(verify_life_support_rating(test))
        print(verify_life_support_rating(data))