input_filename = 'input.txt'
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

def transpose_board(board):
    return [[row[i] for row in board] for i in range(len(board[0]))]


def check_solved(board, drawn_nums):
    if len(drawn_nums) < len(board[0]):
        return False
    for row in board:
        solved = True
        for col in row:
            if col not in drawn_nums:
                solved = False
                break
        if solved:
            return True
    return False


def score_board(board, drawn_nums):
    sum = 0
    for row in board:
        for col in row:
            if col not in drawn_nums:
                sum += col
                print(sum)
    final_num = drawn_nums[-1]
    return sum*final_num


# print(number_draws)
# print(boards)

winning_score = None
winning_board = None

drawn_nums = []
for draw in number_draws:
    drawn_nums.append(draw)
    if(len(drawn_nums) >= board_size):
        for board in boards:
            if(check_solved(board, drawn_nums)):
                winning_board = board
                winning_score = score_board(board, drawn_nums)
                break
            else:
                transposed_board = transpose_board(board)
                if(check_solved(transposed_board, drawn_nums)):
                    winning_board = board
                    winning_score = score_board(transposed_board, drawn_nums)
                    break
    if winning_board:
        break

# print(winning_board)
print(winning_score)