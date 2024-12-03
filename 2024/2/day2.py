input_filename = 'input.txt'

def is_changing(cur_level, next_level, increasing):
    if cur_level == next_level:
        return False
    if increasing:
        if cur_level < next_level and cur_level+1 <= next_level and cur_level+3 >= next_level:
            return True
    if not increasing:
        if cur_level > next_level and cur_level-1 >= next_level and cur_level-3 <= next_level:
            return True
    return False

def is_safe(levels):
    if levels[0] == levels[1]:
        return False
    elif levels[0] < levels[1]:
        increasing = True
    else:
        increasing = False
    for i in range(len(levels)-1):
        if not is_changing(levels[i], levels[i+1], increasing):
            return False
    return True

with open(input_filename) as input_file:
    safe_count = 0
    for line in input_file:
        levels = [int(item) for item in line.split()]
        # print("Checking level")
        # print(levels)
        if is_safe(levels):
            # print("Safe without removing any levels")
            safe_count += 1
        else:
            unsafe_tries = 0
            # print("Trying problem damper")
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if is_safe(new_levels):
                    # print("Safe after removing " + str(str(levels[i])))
                    safe_count += 1
                    break

    print(safe_count)