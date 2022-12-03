import read

def part1():
    calories = read.from_file("day1_input.txt")
    calorie_sum = [0]
    for c in calories:
        if c == "":
            calorie_sum.append(0)
        else:
            calorie_sum[-1] += int(c)
    print(max(calorie_sum))

def part2():
    with open("day1_input.txt") as data:
        input = data.read().split("\n\n")
        calories_by_elf = [line.split("\n") for line in input]
        print(calories_by_elf)
        # elf = ['1000', '2000', '3000']
        calorie_sum = [sum([int(item) for item in elf]) for elf in calories_by_elf]

        print(sum(calorie_sum[-3:]))


part2()