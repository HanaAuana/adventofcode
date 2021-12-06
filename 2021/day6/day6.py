input_filename = 'input.txt'
num_days = 80
incubation_time = 6
newborn_time = 8

initial_string = ''
with open(input_filename) as input_file:
    for line in input_file:
        initial_string = line.strip()

initial_state = [int(i) for i in initial_string.split(',')]

# Part 1
starting_state = initial_state
num_fish = len(starting_state)
for day in range(num_days):
    new_state = list(starting_state)
    for i, fish in enumerate(starting_state):
        if fish == 0:
            new_state[i] = incubation_time
            new_state.append(newborn_time)
        else:
            new_state[i] -= 1
    starting_state = new_state
    num_fish = len(starting_state)

print(num_fish)


# Part 2
fish_counts = [0 for i in range(newborn_time+1)]
starting_state = initial_state

for fish in starting_state:
    fish_counts[fish] += 1

num_days = 256
for day in range(num_days):
    new_fish = fish_counts.pop(0)
    fish_counts[incubation_time] += new_fish
    fish_counts.append(new_fish)

num_fish = sum(fish_counts)
print(num_fish)