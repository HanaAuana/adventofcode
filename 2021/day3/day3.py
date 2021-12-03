input_filename = 'input.txt'

original_candidates = []

def get_most_common_bits(input_list):
    list_size = len(input_list)
    line_size = len(input_list[0].strip())
    set_bit_counts = [0 for i in range(line_size)]

    for line in input_list:
        for index, bit in enumerate(line):
            if bit == '1':
                set_bit_counts[index] += 1
    return ['1' if set_bit_counts[i] >= list_size/2 else '0' for i in range(line_size)]

def reverse_bits(input_list):
    return  [str(int(i) ^1) for i in input_list] 

# Part 1
with open(input_filename) as input_file:
    for line in input_file:
        original_candidates.append(line.strip())

most_common_bits = get_most_common_bits(original_candidates)

gamma_value = ''.join(most_common_bits)
epsilon_value = ''.join('1' if b == '0' else '0' for b in gamma_value)

print(int(gamma_value, 2)*int(epsilon_value, 2))


# Part 2
oxygen_rating = None
co2_rating = None
line_length = len(original_candidates[0].strip())

possible_candidates = list(original_candidates)
new_candidates = []
common_bits = most_common_bits

for i in range(line_length):
    for line in possible_candidates:
        if int(line[i]) == int(common_bits[i]):
            new_candidates.append(line)
    if len(new_candidates) == 1:
        oxygen_rating = new_candidates[0]
        break
    else:
        common_bits = get_most_common_bits(new_candidates)
        possible_candidates = new_candidates
        new_candidates = []


possible_candidates = list(original_candidates)
new_candidates = []
least_common_bits = reverse_bits(most_common_bits) 
for i in range(line_length):
    for line in possible_candidates:
        if int(line[i]) == int(least_common_bits[i]):
            new_candidates.append(line)
    if len(new_candidates) == 1:
        co2_rating = new_candidates[0]
        break
    possible_candidates = new_candidates
    least_common_bits = reverse_bits(get_most_common_bits(possible_candidates))
    new_candidates = []



print(int(oxygen_rating, 2)*int(co2_rating, 2))