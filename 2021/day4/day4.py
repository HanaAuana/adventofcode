import copy

input_filename = 'input.txt'
board_size = 5

next_board_num = -1
next_row_num = 0

number_draws = []
boards = []


# Part 1
with open(input_filename) as input_file:
    for i, line in enumerate(input_file):
        if i == 0:
            number_draws = [int(n) for n in line.split(',')]
        elif line.strip() == '':
            pass
        else:
            if next_row_num == 0:
                boards.append([])
                next_board_num += 1
            boards[next_board_num].append([int(n) for n in line.split()])
            next_row_num += 1
            if next_row_num == board_size:
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
    final_num = drawn_nums[-1]
    return sum*final_num



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

print(winning_score)


last_board = None

next_boards = copy.deepcopy(boards)
remaining_boards = next_boards

drawn_nums = []
for draw in number_draws:
    drawn_nums.append(draw)
    if(len(drawn_nums) >= board_size):
        for i, board in enumerate(remaining_boards):
            if(check_solved(board, drawn_nums)):
                last_board = next_boards.pop(i)
                if len(remaining_boards) == 1:
                    break
            else:
                transposed_board = transpose_board(board)
                if(check_solved(transposed_board, drawn_nums)):
                    last_board = next_boards.pop(i)
                    if len(remaining_boards) == 1:
                        break
    if len(next_boards) == 0:
        break
    next_boards = copy.deepcopy(remaining_boards)
    remaining_boards = next_boards

    

print(score_board(last_board, drawn_nums))