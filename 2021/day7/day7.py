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

# Part 2
best_fuel_change = None
best_pos = initial_state[0]

for target in range(min(initial_state), max(initial_state)):
    # print(f'Trying {target}')
    this_fuel_change = 0
    for crab in initial_state:
        this_crab_change = sum(range(int(abs(target-crab))+1))
        # print(f'Moving from {crab} takes {this_crab_change}')
        this_fuel_change += this_crab_change
    # print(this_fuel_change)
    if not best_fuel_change or this_fuel_change < best_fuel_change:
        best_fuel_change = this_fuel_change
        best_pos = target

print(best_pos)
print(best_fuel_change)


11