input_filename = 'day1_input.txt'

left_list = []
right_list = []

left_freq = {}
right_freq = {}

with open(input_filename) as input_file:
    for line in input_file:
        locations = line.split()
        left_item = int(locations[0])
        right_item = int(locations[1])
        left_list.append(left_item)
        if left_item in left_freq:
            left_freq[left_item] += 1
        else:
            left_freq[left_item] = 1
        right_list.append(right_item)
        if right_item in right_freq:
            right_freq[right_item] += 1
        else:
            right_freq[right_item] = 1
left_list.sort()
right_list.sort()

differences_total = 0
similarity_score_total = 0
for i in range(len(left_list)):
    differences_total += abs(left_list[i] - right_list[i])
    if left_list[i] in right_freq:
        similarity_score_total += (left_list[i] * right_freq[left_list[i]])
print(differences_total)
print(similarity_score_total)