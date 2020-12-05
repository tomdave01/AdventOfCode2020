from Day3 import TreesEncountered

right1 = TreesEncountered(1, 'Day3_input.txt', 1, 1)
right3 = TreesEncountered(3, 'Day3_input.txt', 1, 1)
right5 = TreesEncountered(5, 'Day3_input.txt', 1, 1)
right7 = TreesEncountered(7, 'Day3_input.txt', 1, 1)
down2 = TreesEncountered(1, 'Day3_input.txt', 2, 2)

print(right1*right3*right5*right7*down2)
