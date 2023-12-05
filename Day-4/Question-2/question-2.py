def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            lines.append(line.rstrip())
    return lines

def process_data(data):
    changed = False
    for d in data:
        if d == '' or d == ' ':
            data.remove(d)
            changed = True
    return changed

def check_matching_numbers(main_set, secondary_set):
    num_matching = 0
    for n in secondary_set:
        if n in main_set and n != '':
            num_matching = num_matching + 1
    return num_matching

def process_card(line):
    card_number = line.split(':')
    card_number_int = card_number[0].split(' ')[-1]
    number_sets = card_number[1].split('|')
    set_1 = number_sets[0].split(' ')
    set_2 = number_sets[1].split(' ')
    processed1 = True
    processed2 = True
    while processed1:
        processed1 = process_data(set_1)
    while processed2:
        processed2 = process_data(set_2)
    return (card_number_int, set_1, set_2)
    

def parse_data(lines):
    cards = {}
    for l in lines:
        card = process_card(l)
        # Card[<card_number>] = (<card_number>, set_1, set_2)
        cards[card[0]] = (card[0], card[1], card[2])
    return cards
    
def check_card(card):
    return check_matching_numbers(card[1], card[2])

def increment_occurance(occurances, start_index, num_increment):
    for i in range(start_index, start_index + num_increment):
        occurances[i-1] = occurances[i-1] + 1

def get_sum(nums):
    total = 0
    for n in nums:
        total = total + int(n)
    return total

data = read_from_txt("data.txt")
cards = parse_data(data)
occurance_list = [1] * len(cards)

# Set First Copy to 1 Occurance
# Check_Card(1) = 4
# increment occurance for next 4 cards (2, 3, 4, 5)
# process card 2
# Check_Card(2) = 2 * occurances
# increment x2

for key in cards:
    card = cards[key]
    matches = check_card(card)
    occurances = occurance_list[int(key)-1]
    # print(occurances)
    print("Card: " + key + " Matches: " + str(matches) + " Occurances: " + str(occurances))
    for i in range(0, occurances):
        increment_occurance(occurance_list, int(key) + 1, matches)
print(get_sum(occurance_list))
