# 1. Strip all Letters out
# 2. Concatenate first + last
# 3. Add Together
# 4. Return output to terminal

import re

def strip_letters(s: str):
    s2 = re.sub(r'[^\d]', '', s)
    return s2

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
        stripped_data.append(strip_letters(d))
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