input_filename = 'input.txt'

# Part 1
with open(input_filename) as input_file:
    pos_horiz = 0
    pos_depth = 0
    for line in input_file:
        direction, move = line.split(' ')
        move = int(move)
        if direction == 'forward':
            pos_horiz += move
        elif direction == 'down':
            pos_depth += move
        elif direction == 'up':
            pos_depth -= move
    pos_final = pos_depth * pos_horiz
    print(pos_final)

# Part 2
with open(input_filename) as input_file:
    aim = 0
    depth = 0
    pos_horiz = 0
    for line in input_file:
        direction, move = line.split(' ')
        move = int(move)
        if direction == 'forward':
            pos_horiz += move
            depth += move*aim
        elif direction == 'down':
            aim += move
        elif direction == 'up':
            aim -= move
    pos_final = depth * pos_horiz
    print(pos_final)