def SumTo2020():
    with open('Day1_input.txt', 'r') as file:
        numbers = file.readlines()
    for i in range(len(numbers)):
        additive = int(numbers[i].strip())
        for num in numbers:
            if (additive + int(num.strip()) == 2020):
                return additive * int(num.strip())

print(SumTo2020())