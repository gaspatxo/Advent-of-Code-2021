import pandas as pd

readings = pd.read_csv("D2_input.txt", sep=' ')

forward = readings[readings['OPERATION'] == 'forward']['VALUE'].sum()
up = readings[readings['OPERATION'] == 'up']['VALUE'].sum()
down = readings[readings['OPERATION'] == 'down']['VALUE'].sum()

result = forward * (down - up)
print(result)