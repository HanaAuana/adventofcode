input_filename = 'day1-input.txt'

increase_counter = 0
with open(input_filename) as input_file:
    prev_line = None
    for line in input_file:
        cur_line = int(line)
        if prev_line:
            if cur_line > prev_line:
                increase_counter += 1
        prev_line = cur_line

print(increase_counter)