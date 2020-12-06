def ValidPassports(file):
    valid = 0
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    with open(file, 'r') as file:
        lines = file.readlines()
    fields_present = 0
    country = False
    for line in lines:
        line = line.rstrip()
        if line == "":
            if ((fields_present == 7) and (not country)) or (fields_present == 8):
                valid += 1
            fields_present = 0
            country = False
            continue
        else:
            for field in valid_fields:
                if field in line:
                    fields_present += 1
                    if field == 'cid':
                        country = True
        print('fields', fields_present, 'cid', country, 'valid', valid)

    return valid

print(ValidPassports('Day4_input.txt'))