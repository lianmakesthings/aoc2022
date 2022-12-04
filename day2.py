import read


def part1(file_path):
    points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3 }
    winning = {"A": "Y", "B": "Z", "C": "X"}
    input = [line.split(' ') for line in read.from_file(file_path)]
    score = 0
    for round in input:
        opponent = round[0]
        you = round[1]
        score += points[you]
        
        if points[opponent] == points[you]:
            score += 3
        else:
            if winning[opponent] == you:
                score += 6
    return score

def part2(file_path):
    points = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6 }
    input = [line.split(' ') for line in read.from_file(file_path)]
    
    score = 0
    for round in input:
        opponent = round[0]
        result = round[1]

        score += points[result]
        if result == "Y":
            score += points[opponent]

        elif result == "Z":
            score += points[opponent] % 3 + 1

        # 1 => 3 | 0 % 3 
        # 2 => 1 | 1 % 3
        # 3 => 2 | 2 % 3

        else:
            score += 3 if opponent == "A" else points[opponent] - 1 % 3

    return score

print(part2("day2_input.txt"))