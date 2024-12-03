import re

# reg_pattern = r'mul\((\d+,\d+)\)'
reg_pattern = r'mul\((\d+,\d+)\)|(do\(\))|(don\'t\(\))'

input_filename = 'input.txt'

sum

with open(input_filename) as input_file:
    input_text = input_file.read()
    captures = re.findall(reg_pattern, input_text)
    matches = [item for tup in captures for item in tup if item]
    do_include = True
    sum = 0
    for match in matches:
        if match == "don't()":
            do_include = False
        elif match == 'do()':
            do_include = True
        elif type(match[0] is int):
            operands = match.split(',')
            if do_include:
                sum += int(operands[0]) * int(operands[1])

    print(sum)