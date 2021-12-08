input_filename = 'input.txt'

initial_string = ''

with open(input_filename) as input_file:
    for line in input_file:
        initial_string += line

lines = [i.split('|') for i in initial_string.split('\n')]

# print(lines)

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


# Part 2
total = 0
output_values = []
for signals, output in lines:
    keys = ['' for i in range(10)]
    four_diff_one = ''
    for signal in sorted(signals.split(), key=len):
        clear_signal = signal.strip()
        sorted_signal = ''.join(sorted(clear_signal))
        if len(clear_signal) == 2:
                keys[1] = sorted_signal
                continue
        elif len(clear_signal) == 3:
            keys[7] = sorted_signal
            continue
        elif len(clear_signal) == 4:
            keys[4] = sorted_signal
            four_diff_one = ''.join([c for c in list(keys[4]) if c not in keys[1]])
            continue
        elif len(clear_signal) == 7:
            keys[8] = sorted_signal
            continue
        elif len(clear_signal) == 5:
            if set(keys[1]) <= set(clear_signal):
                keys[3] = sorted_signal
            else:
                if set(four_diff_one) <= set(clear_signal):
                    keys[5] = sorted_signal
                else:
                    keys[2] = sorted_signal
        elif len(clear_signal) == 6:
            if set(keys[1]) <= set(clear_signal):
                if set(keys[4]) <= set(clear_signal):
                    keys[9] = sorted_signal
                else:
                    keys[0] = sorted_signal
            else:
                keys[6] = sorted_signal


    sorted_outputs = [''.join(sorted(o)) for o in output.split()]
    display = ''
    for value in sorted_outputs:
        for i,key in enumerate(keys):
            if value == key:
                display += str(i)
    total += int(display)
        
print(total)