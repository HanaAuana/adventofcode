input_filename = 'test.txt'

initial_string = ''

with open(input_filename) as input_file:
    for line in input_file:
        initial_string += line

lines = [i.split('|') for i in initial_string.split('\n')]

print(lines)

# Part 1
counts = [0 for i in range(10)]
for signals, output in lines:

    for value in output.split():
        if len(value.strip()) == 2:
            counts[1] += 1
            continue
        elif len(value.strip()) == 3:
            counts[7] += 1
            continue
        elif len(value.strip()) == 4:
            counts[4] += 1
            continue
        elif len(value.strip()) == 7:
            counts[8] += 1
            continue

print(sum((counts[1], counts[4], counts[7], counts[8])))
