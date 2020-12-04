def TreesEncountered(file):
    count = 3
    tree_count = 0
    with open(file, 'r') as file:
        lines = file.readlines() #read the lines into lists
    for i in range(1, len(lines)): #traverse through the lists
        line = lines[i] #make the line the new variable for list items
        line = line.rstrip() #strip the newline off of the list items
        if count not in range(-len(line), len(line)): #check if count index is within the list item
            print(len(line), count)
            count = 1 #reset the count
            continue #restart the loop
        elif line[count] == '#': #check if there's a tree
            tree_count += 1 #Count the tree
        count += 3 #add 3 for the next line
    return tree_count
print(TreesEncountered('Day3_input.txt'))