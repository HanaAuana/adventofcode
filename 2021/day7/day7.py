from statistics import median

input_filename = 'input.txt'

initial_string = ''
with open(input_filename) as input_file:
    for line in input_file:
        initial_string = line.strip()

initial_state = [int(i) for i in initial_string.split(',')]

# print(initial_state)

# Part 1
target_pos = median(initial_state)
total_change = 0

for crab in initial_state:
    total_change += abs(target_pos-crab)

print(total_change)