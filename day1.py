
def part1():
    with open('day1_input.txt') as data:
        calories = [line.strip() for line in data.readlines()]
        calorie_sum = [0]
        for c in calories:
            if c == "":
                calorie_sum.append(0)
            else:
                calorie_sum[-1] += int(c)
        print(max(calorie_sum))

def part2():
    with open('day1_input.txt') as data:
        calories = [line.strip() for line in data.readlines()]
        calorie_sum = [0]
        for c in calories:
            if c == "":
                calorie_sum.append(0)
            else:
                calorie_sum[-1] += int(c)

        calorie_sum.sort(reverse=True)
        print(sum(calorie_sum[0:3]))

part2()