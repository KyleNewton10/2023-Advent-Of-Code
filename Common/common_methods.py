def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            lines.append(line.rstrip())
    return lines

