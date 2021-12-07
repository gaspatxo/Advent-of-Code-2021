increase_counter = 0

with open('W1_P1_input.txt', 'r') as f:
    clean_list = [int(line) for line in f.readlines()]

for i in range(len(clean_list)-1):
    if clean_list[i+1] > clean_list[i]:
        increase_counter += 1
print(increase_counter)
