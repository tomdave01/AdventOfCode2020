def TreesEncountered(right, file, start, step):
    count = 0
    tree_count = 0
    with open(file, 'r') as file:
        lines = file.readlines() #read the lines into lists
    for i in range(start, len(lines), step): #traverse through the lists
        count += right #add right steps for the next line
        line = lines[i] #make the line the new variable for list items
        line = line.rstrip() #strip the newline off of the list items
        if count > 30 : #check if count index is within the list item
            count %= len(line) #reset the count
            if line[count] == '#': #check if there's a tree
                tree_count += 1 #Count the tree
            continue #restart the loop
        elif line[count] == '#': #check if there's a tree
            tree_count += 1 #Count the tree
    return tree_count
