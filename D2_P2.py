import pandas as pd

readings = pd.read_csv("D2_input.txt", sep=' ')

forward = readings[readings['OPERATION'] == 'forward']['VALUE'].sum()

def calculate_aim(row):
    operation = row["OPERATION"]
    if operation == "forward":
        return 0
    elif operation == "up":
        return -1*int(row["VALUE"])
    elif operation == "down":
        return int(row["VALUE"])
    return "Something went wrong"

new_column = []

prev_val = 0
for x in readings.apply(calculate_aim,axis=1):
    x += prev_val
    prev_val = x
    new_column.append(x)

depth = 0
for index,row in readings[readings['OPERATION'] == 'forward'].iterrows():
    depth += int(row["VALUE"])*new_column[index]

print(depth*forward)