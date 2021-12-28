import numpy as np

with open("D3_input.txt", 'r') as input_f:
    input = np.array([list(x.replace('\n','')) for x in input_f.readlines()]).astype(np.int)
row_number = input.shape[0]

gamma = int("".join(str(x) for x in [round(sum(input[:,x])/row_number) for x in range(input.shape[1])]), 2)
epsilon = (~gamma)&(2^12)  #Create complement

print(gamma*epsilon)