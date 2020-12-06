def ValidPassports(file):
    valid = 0
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    with open(file, 'r') as file:
        lines = file.readlines()
    fields_present = 0 #Number of fields found in the passport
    country = False #Check for Country ID
    for line in lines: #Loop over the file
        line = line.rstrip() #Strip the file of the newline character
        if line == "": #Check if we're at the end of one Block 
            if ((fields_present == 7) and (not country)) or (fields_present == 8): #Check if the conditions for validity are met
                valid += 1
            fields_present = 0 #Reset the parameters
            country = False #Reset the parameters
            continue
        else: #If we're within a Block
            for field in valid_fields: #iterate through the valid fields to check the passports
                if field in line: 
                    fields_present += 1 #Confirm that a field for validity is present
                    if field == 'cid': 
                        country = True #If the field has Country ID

    return valid

print(ValidPassports('Day4_input.txt'))