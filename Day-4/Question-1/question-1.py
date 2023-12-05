def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            lines.append(line.rstrip())
    return lines

def process_data(data):
    for d in data:
        if d == '' or d == ' ':
            data.remove(d)

def check_winning_numbers(winning_numbers, drawn_numbers):
    points = 0
    for n in drawn_numbers:
        if n in winning_numbers and n != '':
            if points == 0:
                points = 1
            else:
                points = points * 2
    return points

def get_sum(nums):
    total = 0
    for n in nums:
        total = total + int(n)
    return total

def process(line):
    card_number = line.split(':')
    l2 = card_number[1].split('|')
    winning_numbers = l2[0].split(' ')
    drawn_numbers = l2[1].split(' ')
    process_data(winning_numbers)
    process_data(drawn_numbers)
    return check_winning_numbers(winning_numbers, drawn_numbers)

def parse_data(lines):
    points = 0
    for l in lines:
        points = points + process(l)
    return points
    



data = read_from_txt("data.txt")
points = parse_data(data)
print(points)