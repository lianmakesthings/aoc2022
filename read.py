def from_file(file_path):
    with open(file_path) as data:
        return [line.strip() for line in data.readlines()]