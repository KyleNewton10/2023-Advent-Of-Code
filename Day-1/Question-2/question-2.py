# 1. Replace all spelled out numbers
# 2. Strip all Letters
# 3. Concatenate first + last
# 4. Add Together
# 5. Return output to terminal

import re

def substitute_one(s: str):
    return s.replace('one', 'on1e')

def substitute_two(s: str):
    return s.replace('two', 'tw2o')

def substitute_three(s: str):
    return s.replace('three', 'thre3e')

def substitute_four(s: str):
    return s.replace('four', 'fou4r')

def substitute_five(s: str):
    return s.replace('five', 'fiv5e')

def substitute_six(s: str):
    return s.replace('six', 'si6x')

def substitute_seven(s: str):
    return s.replace('seven', 'seve7n')

def substitute_eight(s: str):
    return s.replace('eight', 'eigh8t')

def substitute_nine(s: str):
    return s.replace('nine', 'nin9e')

def strip_letters(s: str):
    s2 = re.sub(r'[^\d]', '', s)
    return s2

def sub_numbers(s: str):
    subbed = substitute_one(s)
    subbed = substitute_two(subbed)
    subbed = substitute_three(subbed)
    subbed = substitute_four(subbed)
    subbed = substitute_five(subbed)
    subbed = substitute_six(subbed)
    subbed = substitute_seven(subbed)
    subbed = substitute_eight(subbed)
    subbed = substitute_nine(subbed)
    return subbed

def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            lines.append(line.rstrip())
    return lines

def read_and_strip_data():
    data = read_from_txt("data.txt")
    stripped_data = []
    for d in data:
        stripped_data.append(strip_letters(sub_numbers(d)))
    return stripped_data

def get_calibration_value(v):
    first = v[0]
    last = v[-1]
    return str(first) + str(last)

def get_calibration_values(values):
    calibration_values = []
    for v in values:
        calibration_values.append(get_calibration_value(v))
    return calibration_values

def add_calibration_values(values):
    total = 0
    for v in values:
        total = total + int(v)
    return total

data = read_and_strip_data()
cali_values = get_calibration_values(data)
total = add_calibration_values(cali_values)
print(total)