input_filename = 'day1-input.txt'

# Part 1
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


# Part 2
increase_counter = 0
with open(input_filename) as input_file:
    prev_line_2 = None
    prev_line_1 = None
    prev_sum = None
    for line in input_file:
        cur_line = int(line)
        if prev_line_1 and prev_line_2:
            cur_sum = cur_line + prev_line_1 + prev_line_2
            if prev_sum:
                if cur_sum > prev_sum:
                    increase_counter += 1
            prev_sum = cur_sum
        prev_line_2 = prev_line_1
        prev_line_1 = cur_line
print(increase_counter)