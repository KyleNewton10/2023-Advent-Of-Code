# 1. Strip all Letters out
# 2. Concatenate first + last
# 3. Add Together
# 4. Return output to terminal

import re

def strip_letters(s: str):
    s2 = re.sub(r'[^\d]', '', s)
    return s2

def read_from_txt(fileName: str):
    with open(fileName) as openedFile:
        lines = [line.rstrip() for line in openedFile]