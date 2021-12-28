DAYS = 256

fishes = {
    8: 0,
    7: 0,
    6: 0,
    5: 0,
    4: 0,
    3: 0,
    2: 0,
    1: 0,
    0: 0
}
with open("D6_input.txt") as file:
    for fish in [int(str_fish) for str_fish in file.readline().rstrip('\n').split(',')]:
        fishes[fish] += 1

for _ in range(DAYS):
    new_fish = fishes[0]
    for timer in range(1,9):
        fishes[timer-1] = fishes[timer]
    fishes[8] = new_fish
    fishes[6] += new_fish

total_fish = sum(fishes.values())
print(total_fish)