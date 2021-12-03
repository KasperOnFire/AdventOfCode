from pathlib import Path


def calculate_gamma_and_epsilon(inputs: list[str]) -> int:
    threshold = len(inputs) / 2
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
    bit_length = len(inputs[0])
    oxygen_values = inputs

    for i in range(bit_length):
        if len(oxygen_values) == 1:
            break
        count_1 = 0
        values_1 = []
        values_0 = []
        threshold = len(oxygen_values) / 2
        for bit in oxygen_values:
            if bit[i] == "1":
                count_1 += 1
                values_1.append(bit)
            else:
                values_0.append(bit)
            oxygen_values = values_1 if count_1 >= threshold else values_0

    co2_values = inputs

    for i in range(bit_length):
        if len(co2_values) == 1:
            break
        co2_count_1 = 0
        co2_values_1 = []
        co2_values_0 = []
        co2_threshold = len(co2_values) / 2
        for bit in co2_values:
            if bit[i] == "1":
                co2_count_1 += 1
                co2_values_1.append(bit)
            else:
                co2_values_0.append(bit)
        co2_values = co2_values_1 if co2_count_1 < co2_threshold else co2_values_0

    oxygen_generator_rating = int(oxygen_values[0], 2)
    co2_scrubber_rating = int(co2_values[0], 2)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    with open(Path("../Data/Day3Input.txt"), 'r') as f:
        data = [x for x in f.read().splitlines()]
        test = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                "01010"]

        # print(calculate_gamma_and_epsilon(test))
        print(calculate_gamma_and_epsilon(data))

        # print(verify_life_support_rating(test))
        print(verify_life_support_rating(data))
