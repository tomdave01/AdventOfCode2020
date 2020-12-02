import re

def PasswordScreener(file):
    second_counter = 0
    with open(file, 'r') as file:
        for line in file:
            line = line.rstrip()
            parameters = re.compile(r'\w+')
            parameters = parameters.findall(line)
            counter = 0
            for char in parameters[3]:
                if char == parameters[2]:
                    counter += 1
            if (counter >= int(parameters[0])) and (counter <= int(parameters[1])):
                second_counter += 1

    return second_counter
            
print(PasswordScreener('Day2_input.txt'))