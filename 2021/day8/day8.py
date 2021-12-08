input_filename = 'test.txt'

initial_string = ''

with open(input_filename) as input_file:
    for line in input_file:
        initial_string += line

lines = [i.split('|') for i in initial_string.split('\n')]

print(lines)