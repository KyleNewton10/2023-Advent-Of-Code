num_red_cubes = 12
num_green_cubes = 13
num_blue_cubes = 14

def check_if_valid_numbers(red, green, blue):
    rTrue = False
    gTrue = False
    bTrue = False
    if red <= num_red_cubes:
        rTrue = True
    if green <= num_green_cubes:
        gTrue = True
    if blue <= num_blue_cubes:
        bTrue = True
    return (rTrue and gTrue and bTrue)

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



data = read_from_txt("data.txt")
data = extract_games(data)
games = []
id_total = 0
for d in data:
    games.append(transform_single_game_data(d))
for i in range(0, len(games)):
    game = games[i]
    isValidGame = True
    for draw in game:
        #print("Game: " + str(i+1) + " - Draw: " + str(draw))
        valid = check_if_valid_numbers(int(draw[0]), int(draw[1]), int(draw[2]))
        #print(valid)
        if not valid:
            isValidGame = False
    if isValidGame:
        #print("Game " + str(i+1) + " is valid")
        id_total = id_total + (i + 1)
    isValidGame = True
print(id_total)