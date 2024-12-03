import re

reg_pattern = r'mul\((\d+,\d+)\)'

input_filename = 'input.txt'

sum

with open(input_filename) as input_file:
    input_text = input_file.read()
    matches = [item.split(',') for item in re.findall(reg_pattern, input_text)]
    print(sum(int(item[0])*int(item[1]) for item in matches))