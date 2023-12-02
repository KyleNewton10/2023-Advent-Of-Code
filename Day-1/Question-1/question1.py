# 1. Strip all Letters out
# 2. Concatenate first + last
# 3. Add Together
# 4. Return output to terminal

def strip_letters(s: str):
    re.sub(r'[\d.*\d]', '', s)
    print(s)

strip_letters("1abc2")