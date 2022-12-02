
with open("input.txt", "r") as f:
    lines = f.readlines()
score = 0
for line in lines:
    if line[0] == "A" and line[2] == "X":
        score += 3
    elif line[0] == "A" and line[2] == "Y":
        score += 4
    elif line[0] == "A" and line[2] == "Z":
        score += 8
    elif line[0] == "B" and line[2] == "X":
        score += 1
    elif line[0] == "B" and line[2] == "Y":
        score += 5
    elif line[0] == "B" and line[2] == "Z":
        score += 9
    elif line[0] == "C" and line[2] == "X":
        score += 2
    elif line[0] == "C" and line[2] == "Y":
        score += 6
    elif line[0] == "C" and line[2] == "Z":
        score += 7
print(score)


