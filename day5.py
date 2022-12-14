import re

def open_file(file_name):
    with open(file_name) as data:
        return [line.replace("\n", "") for line in data.readlines()]

def build_ship(file_name):
    input = open_file(file_name)
    crates = [[] for i in range(len(input[0])//3)]
    input.reverse()
    for line in input:
        c = 0
        for i in range(1, len(line), 4):
            if line[i] != " ":
                crates[c].append(line[i])
            c += 1
    return crates

def parse_instructions(file_name):
    input = open_file(file_name)
    instructions = []
    for line in input:
        instructions.extend([(int(i[0]), int(i[1]), int(i[2])) for i in re.findall("move (\d+) from (\d) to (\d)", line)])
    return instructions

def move_crates(crates, instruction):
    count = instruction[0]
    from_crate = instruction[1]-1
    to_crate = instruction[2]-1
    
    for i in range(count):
        crates[to_crate].append(crates[from_crate].pop())
    return crates

def move_crates_together(crates, instruction):
    count = instruction[0]
    from_crate = instruction[1]-1
    to_crate = instruction[2]-1
    crates_to_move = crates[from_crate][-count:]
    crates[from_crate] = crates[from_crate][:-count]
    crates[to_crate].extend(crates_to_move)
    return crates

def part1(file_name_crates, file_name_instructions):
    crates = build_ship(file_name_crates)
    instructions = parse_instructions(file_name_instructions)
    for instruction in instructions:
        crates = move_crates(crates, instruction)
    return "".join([crate[-1] for crate in crates if len(crate) > 0])

def part2(file_name_crates, file_name_instructions):
    crates = build_ship(file_name_crates)
    instructions = parse_instructions(file_name_instructions)
    for instruction in instructions:
        crates = move_crates_together(crates, instruction)
    return "".join([crate[-1] for crate in crates if len(crate) > 0])

print(part2('day5_input_crates.txt', 'day5_input_instructions.txt'))