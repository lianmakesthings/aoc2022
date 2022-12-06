import read

def part1(filename):
    input = read.from_file(filename)
    overlap_count = 0
    for line in input:
        [elf1, elf2] = [[int(sectionId) for sectionId in elves.split('-')] for elves in line.split(',')]
        elf1 = range(elf1[0], elf1[1]+1)
        elf2 = range(elf2[0], elf2[1]+1)
        if len(set(elf1).intersection(elf2)) == min(len(elf1), len(elf2)):
            overlap_count += 1

    return overlap_count

def part2(filename):
    input = read.from_file(filename)
    overlap_count = 0
    for line in input:
        [elf1, elf2] = [[int(sectionId) for sectionId in elves.split('-')] for elves in line.split(',')]
        elf1 = range(elf1[0], elf1[1]+1)
        elf2 = range(elf2[0], elf2[1]+1)
        if len(set(elf1).intersection(elf2)) > 0:
            overlap_count += 1
    return overlap_count

print(part2('day4_input.txt'))
print(type(range(4)))