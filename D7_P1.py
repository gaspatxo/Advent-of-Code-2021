import numpy as np

with open("D7_input.txt") as file:
    crabs = [int(str_crab_pos)
             for str_crab_pos in file.readline().rstrip("\n").split(",")]

CRAB_NUM = len(crabs)
POSITION_RANGE = (min(crabs), max(crabs))

dp = np.zeros((CRAB_NUM, POSITION_RANGE[1]-POSITION_RANGE[0]+1), dtype=np.uint64)

for crab_index,crab in enumerate(crabs):
    for position in range(POSITION_RANGE[0],POSITION_RANGE[1]+1):
        distance = abs(position - crabs[crab_index])
        if crab_index == 0:
            dp[crab_index,position] = distance  # Calculate cost
        else:
            dp[crab_index,position] = distance + dp[crab_index - 1,position] # Calculate cost

print(min(dp[-1]))