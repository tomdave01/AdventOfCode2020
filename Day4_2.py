import re

def ValidPassports(file):
    valid = 0
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    with open(file, 'r') as file:
        lines = file.readlines()
    fields_present = 0 #Number of fields found in the passport
    country = False

    for line in lines: #Loop over the file
        line = line.rstrip() #Strip the file of the newline character
        if line == "":
            #Reset Variables here
            if ((fields_present == 7) and (country == False)) or (fields_present == 8):
                valid += 1
            country = False
            d.clear()
            fields_present = 0
        else: #If we're within a Block
            if " " in line:
                d = dict(x.split(':') for x in line.split(' '))
            else:
                line = line.split(':', 2)
                d = dict({line[0]:line[1]})

            for field in valid_fields: #iterate through the valid fields to check the passports
                if field in d.keys():
                    if field == 'cid':
                        country = True
                        fields_present += 1
                    elif field == 'byr':
                        match_byr = re.match(r'(19[2-9][0-9])|(200[0-2])', d[field])
                        if match_byr:
                            fields_present += 1
                    elif field == 'iyr':
                        match_iyr = re.match(r'(201[0-9])|(2020)', d[field])
                        if match_iyr:
                            fields_present +=1
                    elif field == 'eyr':
                        match_eyr = re.match(r'(202[0-9])|(2030)', d[field])
                        if match_eyr:
                            fields_present += 1
                    elif field == 'hgt':
                        if 'cm' in d[field]:
                            match_hgt = re.match(r'(1[5-8][0-9])|(1[9][1-3])', d[field])
                            if match_hgt:
                                fields_present += 1
                        
                        elif 'in' in d[field]:
                            if (int(d[field].strip('in')) >= 59 ) and (int(d[field].strip('in')) <= 76):
                                fields_present += 1
                    
                    elif field == 'hcl':
                        match_hcl = re.match(r'#[0-9a-f]{6}', d[field])
                        if match_hcl:
                            fields_present += 1
                    elif field == 'ecl':
                        match_ecl = re.match(r'((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))', d[field])
                        if match_ecl:
                            fields_present += 1
                    elif field == 'pid':
                        match_pid = re.match(r'[0-9]{9}', d[field])
                        if match_pid:
                            fields_present += 1

    return valid

print(ValidPassports('Day4_input.txt'))