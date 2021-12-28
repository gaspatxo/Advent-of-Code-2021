import numpy as np

def find_parameter(set, most_common:bool):
    col = 0
    while set.shape[0] != 1:
        print(set)

        row_number = set.shape[0]
        if most_common:
            criteria = round(sum(set[:,col])/row_number + 0.001) #calculate most common value in column
        else:
            criteria = round(1 - sum(set[:,col])/row_number) #calculate least common value in column

        set = set[np.where(set[:,col] == criteria)]
        col += 1

    print(set)
    return int("".join([str(int(x)) for x in set[0]]), 2)

with open("D3_input.txt", 'r') as input_f:
    input = np.array([list(x.replace('\n','')) for x in input_f.readlines()]).astype(np.int)

oxygen = find_parameter(input, True)
co2 = find_parameter(input, False)

print(oxygen)
print(co2)
print(oxygen*co2)
