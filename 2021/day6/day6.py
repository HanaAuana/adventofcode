input_filename = 'input.txt'
num_days = 80
incubation_time = 6
newborn_time = 8

initial_string = ''
with open(input_filename) as input_file:
    for line in input_file:
        initial_string = line.strip()

initial_state = [int(i) for i in initial_string.split(',')]

# print(initial_state)

starting_state = initial_state
# print(f'Initial state: {initial_string}')
num_fish = len(starting_state)
for day in range(num_days):
    new_state = list(starting_state)
    for i, fish in enumerate(starting_state):
        if fish == 0:
            new_state[i] = incubation_time
            new_state.append(newborn_time)
        else:
            new_state[i] -= 1
    # print(f'After {day+1} days: {new_state}')
    starting_state = new_state
    num_fish = len(starting_state)
    if day == 80:
        print(num_fish)

print(num_fish)

