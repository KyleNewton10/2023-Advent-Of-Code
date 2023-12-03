def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            lines.append(line.rstrip())
    return lines

def extract_game(data):
    d2 = data.split(':', 1)[1]
    d3 = d2.split(';')
    return d2

def extract_games(games_data):
    games = []
    for g in games_data:
        games.append(extract_game(g))
    return games

def transform_single_game_data(game):
    draws = game.split(';')
    rgb_array = [0, 0, 0]
    final_draws = []
    for d in draws:
        d2 = d.split(',')
        for d3 in d2:
            d4 = d3.split(' ')
            if d4[2] == 'red':
                rgb_array[0] = d4[1]
            if d4[2] == 'green':
                rgb_array[1] = d4[1]
            if d4[2] == 'blue':
                rgb_array[2] = d4[1]
        final_draws.append(rgb_array)
        rgb_array = [0, 0, 0]
    return final_draws

def get_game_minimums(game):
    minimums = [0, 0, 0]
    for draw in game:
        if int(draw[0]) > int(minimums[0]):
            minimums[0] = draw[0]
        if int(draw[1]) > int(minimums[1]):
            minimums[1] = draw[1]
        if int(draw[2]) > int(minimums[2]):
            minimums[2] = draw[2]
    return minimums

def get_power_set(set):
    return int(set[0]) * int(set[1]) * int(set[2])

def sum_power_set(set):
    total = 0
    for s in set:
        total = total + int(s)
    return total

data = read_from_txt("data.txt")
data = extract_games(data)
games = []
for d in data:
    games.append(transform_single_game_data(d))
minimums = []
for g in games:
    minimums.append(get_game_minimums(g))
power_sets = []
for m in minimums:
    power_sets.append(get_power_set(m))
print(power_sets)
print(sum_power_set(power_sets))