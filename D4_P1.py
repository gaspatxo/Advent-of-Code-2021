import numpy as np
import numpy.ma as ma

def find_winner(masked_tables):
    for number in bingo_numbers:
        masked_tables = ma.masked_equal(masked_tables, number)
        for table in masked_tables:
            for index in range(5):
                if table[index,:].mask.sum() == 5 or table[:,index].mask.sum() == 5:
                    return([table,number])
    return("None found")

with open("D4_input.txt") as file:
    bingo_numbers = [int(x) for x in file.readline().split(",")]
    whole_thing = file.readlines()

tables = []
for i in range(len(whole_thing)//6):
    tables.append(np.array([int(y) for x in whole_thing[1+6*i:6+6*i] for y in x.rstrip("\n").split(" ") if y != ""]).reshape(5,5))
tables = np.array(tables)
result = find_winner(tables)
answer = result[0].sum()*result[1]
print(answer)