def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            l = ['']
            for c in line:
                if c != '\n':
                    l.append(c)
            lines.append(l)
    return lines