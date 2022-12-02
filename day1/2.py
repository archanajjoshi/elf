elf_number = 1
sum_of_calories = 0
highest_calories = 0
highest_calorie_elf_number = 0
total_calories = []
with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        if line != "\n":
            sum_of_calories = sum_of_calories + int(line)
        else:
            total_calories.append(sum_of_calories)
            sum_of_calories = 0

    total_calories.sort(reverse = True)
    total = sum(list(total_calories)[0:3])
    print(total)