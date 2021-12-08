from pathlib import Path


def part_1(circuit_input: list[tuple[str, str]]) -> int:
    number_freq = {num: count for (num, count) in [(x, 0) for x in range(10)]}
    for _, output in circuit_input:
        output_nums = output.split(" ")
        for num in output_nums:
            match len(num):
                case 2:
                    number_freq[1] += 1
                case 3:
                    number_freq[3] += 1
                case 4:
                    number_freq[4] += 1
                case 7:
                    number_freq[8] += 1
                case _:
                    pass
    return sum(number_freq.values())


def part_2(circuit_input: list[tuple[str, str]]) -> int:
    output_values = []
    # Build table of sides
    for input, output in circuit_input:
        val = 0
        # Build decoding table for the sides
        for seq in input.split(" "):
            pass

        # Use to decode output
        for num in output.split(" "):
            pass

        output_values.append(val)
    return sum(output_values)


def run_test():
    test_val = [("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab", "cdfeb fcadb cdfeb cdbaf")]
    print("Test Runs")
    print(part_1(test_val))
    print(part_2(test_val))


run_test()

with open(Path("../Data/Day08Input.txt"), 'r') as f:
    print("Actual Runs")
    data = [(x[0], x[1]) for x in [y.split("|") for y in f.read().splitlines()]]
    print(part_1(data))
    print(part_2(data))
