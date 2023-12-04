import re

def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            l = []
            for c in line:
                if c != '\n':
                    l.append(c)
            lines.append(l)
    return lines

def is_symbol(s: str):
    pattern = re.compile(r'[^0-9]')
    if re.match(pattern, s) and s != '.':
        return True
    return False

def is_number(s: str):
    pattern = re.compile(r'[0-9]')
    if re.match(pattern, s):
        return True
    return False

def is_dot(s: str):
    return s == '.'

def get_symbol_locations(grid):
    symbols = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if is_symbol(grid[y][x]):
                symbol = (x, y)
                symbols.append(symbol)
    return symbols

def get_numbers_and_positions(grid):
    numbers = []
    temp_num = ''
    start_x = -1
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if is_number(grid[y][x]):
                if start_x == -1: start_x = x
                temp_num = temp_num + str(grid[y][x])
            elif is_dot(grid[y][x]) and temp_num != '':
                numbers.append((int(temp_num), start_x, x-1, y))
                temp_num = ''
                start_x = -1
            elif is_symbol(grid[y][x]) and temp_num != '':
                numbers.append((int(temp_num), start_x, x-1, y))
                temp_num = ''
                start_x = -1
        if start_x != -1:
            numbers.append((int(temp_num), start_x, x-1, y))
            temp_num = ''
            start_x = -1
    return numbers

def check_if_number_exists_in_range(xPos, yPos, numbers_list):
    for n in numbers_list:
        if n[3] == yPos:
            if xPos <= n[2] and xPos >= n[1]:
                numbers_list.remove(n)
                return n
    return None

def get_adjacient_values(xPos, yPos, grid, nums):
    temp_nums = nums[:]
    # Not outside Columns
    if xPos != 0 and xPos < len(grid[0])-1:
        # Not Top or Bottom Row
        if yPos != 0 and yPos < len(grid)-1:
            upLeft = check_if_number_exists_in_range(xPos-1, yPos-1, temp_nums)
            up = check_if_number_exists_in_range(xPos-1, yPos, temp_nums)
            upRight = check_if_number_exists_in_range(xPos-1, yPos+1, temp_nums)
            centerLeft = check_if_number_exists_in_range(xPos, yPos-1, temp_nums)
            centerRight = check_if_number_exists_in_range(xPos, yPos+1, temp_nums)
            downLeft = check_if_number_exists_in_range(xPos+1, yPos-1, temp_nums)
            down = check_if_number_exists_in_range(xPos+1, yPos, temp_nums)
            downRight = check_if_number_exists_in_range(xPos+1, yPos+1, temp_nums)
            return ([upLeft, up, upRight], [centerLeft, None, centerRight], [downLeft, down, downRight])
    #Edge Columns
    if xPos == 0:
        if yPos != 0 and yPos < len(grid)-1:
            up = check_if_number_exists_in_range(xPos-1, yPos, temp_nums)
            upRight = check_if_number_exists_in_range(xPos-1, yPos+1, temp_nums)
            centerRight = check_if_number_exists_in_range(xPos, yPos+1, temp_nums)
            down = check_if_number_exists_in_range(xPos+1, yPos, temp_nums)
            downRight = check_if_number_exists_in_range(xPos+1, yPos+1, temp_nums)
            return ([None, up, upRight], [None, None, centerRight], [None, down, downRight])
        elif yPos == 0:
            centerRight = check_if_number_exists_in_range(xPos, yPos+1, temp_nums)
            down = check_if_number_exists_in_range(xPos+1, yPos, temp_nums)
            downRight = check_if_number_exists_in_range(xPos+1, yPos+1, temp_nums)
            return ([None, None, None], [None, None, centerRight], [None, down, downRight])
        elif yPos == len(grid)-1:
            up = check_if_number_exists_in_range(xPos, yPos-1, temp_nums)
            upRight = check_if_number_exists_in_range(xPos+1, yPos-1, temp_nums)
            centerRight = check_if_number_exists_in_range(xPos+1, yPos, temp_nums)
            return ([None, up, upRight], [None, None, centerRight], [None, None, None])
    if xPos == len(grid[0])-1:
        if yPos != 0 and yPos < len(grid)-1:
            upLeft = check_if_number_exists_in_range(xPos-1, yPos-1, temp_nums)
            up = check_if_number_exists_in_range(xPos-1, yPos, temp_nums)
            centerLeft = check_if_number_exists_in_range(xPos, yPos-1, temp_nums)
            downLeft = check_if_number_exists_in_range(xPos+1, yPos-1, temp_nums)
            down = check_if_number_exists_in_range(xPos+1, yPos, temp_nums)
            return ([upLeft, up, None], [centerLeft, None, None], [downLeft, down, None])
        elif yPos == 0:
            centerLeft = check_if_number_exists_in_range(xPos-1, yPos, temp_nums)
            downLeft = check_if_number_exists_in_range(xPos-1, yPos+1, temp_nums)
            down = check_if_number_exists_in_range(xPos-1, yPos-1, temp_nums)
            return ([None, None, None], [centerLeft, None, None], [downLeft, down, None])
        elif yPos == len(grid)-1:
            upLeft = check_if_number_exists_in_range(xPos-1, yPos-1, temp_nums)
            up = check_if_number_exists_in_range(xPos-1, yPos, temp_nums)
            centerLeft = check_if_number_exists_in_range(xPos-1, yPos, temp_nums)
            return ([upLeft, up, None], [centerLeft, None, None], [None, None, None])
        
def get_total_adjacient_values(numbers_list, symbols_list, grid):
    final_total = 0
    print(symbols_list)
    for s in symbols_list:
        xPos = s[0]
        yPos = s[1]
        values = get_adjacient_values(xPos, yPos, grid, numbers_list)
        total = 0
        # print(s)
        #print(values)
        if values is not None:
            for r in values:
                for c in r:
                    if c is not None:
                        total = total + int(c[0])
            final_total = final_total + total
            total = 0
    return final_total


def process_grid(grid):
    symbols = get_symbol_locations(grid)
    #print(symbols)
    numbers = get_numbers_and_positions(grid)
    #print(numbers)
    print(get_total_adjacient_values(numbers, symbols, grid))

    

#grid = read_from_txt("data_small.txt")
grid = read_from_txt("data_large.txt")
#grid = read_from_txt("data_extra.txt")
process_grid(grid)
