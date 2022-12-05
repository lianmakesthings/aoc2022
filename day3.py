import string
import read
def find_duplicate_type(all_compartments):
    return set.intersection(*[set(compartment) for compartment in all_compartments]).pop()

def get_priority(str):
    return string.ascii_letters.index(str)+1

def part1(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            mid_index = len(line)//2
            total += get_priority(find_duplicate_type([line[:mid_index], line[mid_index:]]))
    return total

def part2(filename):
    total = 0
    input = read.from_file(filename)
    for i in range(0, len(input), 3):
        total += get_priority(find_duplicate_type(input[i:i+3]))
    return total

print(part2('day3_input.txt'))