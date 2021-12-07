input_filename = 'test.txt'

initial_string = ''
with open(input_filename) as input_file:
    for line in input_file:
        initial_string = line.strip()

initial_state = [int(i) for i in initial_string.split(',')]

print(initial_state)