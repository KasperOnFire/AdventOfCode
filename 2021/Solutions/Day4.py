from pathlib import Path


def squid_bingo(numbers: list[int], boards: list[list[list[int]]]) -> int:
    checked_numbers = set()
    current_board = [[]]
    for number in numbers:
        checked_numbers.add(number)
        for board in boards:
            current_board = board
            for i in range(5):
                if all(row_numbers in board[i] for row_numbers in checked_numbers):
                    break
                elif all(column_numbers in board[:, i] for column_numbers in checked_numbers):
                    break
        non_marked_numbers = checked_numbers.difference(current_board)
        return sum(non_marked_numbers) * number


if __name__ == '__main__':
    with open(Path("../Data/Day04TestInput.txt"), 'r') as f:
        data = [x for x in f.read().splitlines()]
        input_numbers = [int(x) for x in data[0].split(",")]
        data = data.pop[0:2]
        input_boards = []
        for line in data[, 5]:
            board = []
            board.append(line.split())


    with open(Path("../Data/Day4Input.txt"), 'r') as f:
        pass