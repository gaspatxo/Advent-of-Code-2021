import numpy as np
import numpy.ma as ma


def find_winner(masked_tables, input_numbers):
    remaining_nums = input_numbers.copy()
    for number in input_numbers:
        masked_tables = ma.masked_equal(masked_tables, number)
        for table_index, table in enumerate(masked_tables):
            for index in range(5):
                if table[index, :].mask.sum() == 5 or table[:, index].mask.sum() == 5:
                    return table, table_index, number, remaining_nums
    # Runned out of numbers


with open("D4_input.txt") as file:
    bingo_numbers = [int(x) for x in file.readline().split(",")]
    whole_thing = file.readlines()

tables = []
for i in range(len(whole_thing)//6):
    tables.append(np.array([int(y) for x in whole_thing[1+6*i:6+6*i]
                            for y in x.rstrip("\n").split(" ") if y != ""]).reshape(5, 5))
tables = np.array(tables)
remaining_nums = bingo_numbers

while len(tables) > 0:
    try:
        winner, winner_index, winning_num, remaining_nums = find_winner(
            tables, remaining_nums)
    except:
        print("miuuuuuu")
        break
    tables = np.delete(tables, winner_index, axis=0)


answer = winner.sum()*winning_num
print(answer)
