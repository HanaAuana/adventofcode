input_filename = 'test.txt'
board_size = 5

next_board_num = -1
next_row_num = 0

number_draws = []
boards = []


# Part 1
with open(input_filename) as input_file:
    for i, line in enumerate(input_file):
        # print('Line ' + str(i) +': '+ line.strip())
        if i == 0:
            # print('First row, getting draws')
            number_draws = [int(n) for n in line.split(',')]
        elif line.strip() == '':
            # print('Empty line')
            pass
        else:
            if next_row_num == 0:
                # print(boards)
                # print('Starting a new board')
                boards.append([])
                next_board_num += 1
                # print(boards)
            # print('Add line to current board and advance row num')
            boards[next_board_num].append([int(n) for n in line.split()])
            # print(boards)
            next_row_num += 1
            if next_row_num == board_size:
                # print('Reached end of last board, reset row count')
                next_row_num = 0


print(number_draws)
print(boards)