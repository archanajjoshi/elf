elf_number = 0
sum_of_calories = 0
highest_calories = 0
highest_calorie_elf_number = 0
second_highest_calories = 0
third_highest_calories = 0
with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        if line != "\n":
            sum_of_calories = sum_of_calories + int(line)
        else:
            if sum_of_calories > highest_calories:
                highest_calories = sum_of_calories
                highest_calorie_elf_number = elf_number
            sum_of_calories = 0
            elf_number += 1

print(highest_calorie_elf_number)
print(highest_calories)