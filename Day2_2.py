import re

def PasswordScreener(file):
    second_counter = 0
    with open(file, 'r') as file:
        for line in file:
            line = line.rstrip()
            parameters = re.compile(r'\w+')
            parameters = parameters.findall(line)
            first = int(parameters[0]) - 1
            second = int(parameters[1]) - 1
            if (parameters[3][first] == parameters[2]) ^ (parameters[3][second] == parameters[2]):
                second_counter += 1
    return second_counter
            
print(PasswordScreener('Day2_input.txt'))