import numpy as np

#Get input
coordinates = []
with open("D5_input.txt") as file:
    while (line := file.readline()): #Until the last line
        str_indiv_coords = [str_coordinates.split(",") for str_coordinates in line.rstrip("\n").split(" -> ")]
        coordinates.append([int(str_coordinate) for str_coord_pair in str_indiv_coords for str_coordinate in str_coord_pair])

coordinates = np.array(coordinates)
MAX_X = np.max(coordinates[:,[0,2]])
MAX_Y = np.max(coordinates[:,[1,3]])
covered_points = np.zeros((MAX_X+1,MAX_Y+1), dtype=np.uint8)

#Filter horizontal and vertical lines
for x1,y1,x2,y2 in coordinates:
    if x1 == x2 or y1 == y2: #Horizontal or vertical
        print(x1,y1,x2,y2)
        covered_points[min(y1,y2):max(y1,y2)+1,min(x1,x2):max(x1,x2)+1] += 1
        print(covered_points)
        print()

answer = covered_points[covered_points>1].shape[0] #Filter all greater than 1 get the number
print("\n\n")
print(answer)