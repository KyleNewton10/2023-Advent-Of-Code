def read_from_txt(fileName: str):
    lines = []
    with open(fileName) as openedFile:
        for line in openedFile:
            lines.append(line.rstrip())
    return lines

def clean_raw_data(data):
    seed_data = {}
    clean_data = {}
    for i in range(0, len(data)):
        line = data[i]
        parsing_data = []
        if 'seeds' in line:
            seed_data['seeds'] = line.split(':')[1].split()
        if 'to' in line:
            exitCondition = False
            while line != '' and not exitCondition:
                parsing_data.append(line)
                i = i + 1
                if i == len(data):
                    exitCondition = True
                else:
                    line = data[i]
            clean_data[parsing_data[0].split()[0]] = parsing_data[1:]
    return seed_data, clean_data

def generate_corresponding_map(lines):
    source_set = {}
    for l in lines:
        if l != ' ':
            l2 = l.split()
            dest_range_start = int(l2[0])
            source_range_start = int(l2[1])
            range_length = int(l2[2])
            source_range_set = [i for i in range(source_range_start, source_range_start + range_length)]
            dest_range_set = [i for i in range(dest_range_start, dest_range_start + range_length)]
            for i in range(0, len(source_range_set)):
                source_set[str(source_range_set[i])] = dest_range_set[i]
    return source_set
        


def create_mappings(data):
    mappings = []
    # mapping = (source, destination, mapping_set)
    for k in data:
        conversion = {}
        s2 = k.split('-')
        source_title = s2[0]
        destination_title = s2[-1]
        mappings.append((source_title, destination_title, generate_corresponding_map(data[k])))
    return mappings

def get_location_from_seed(seed, mappings):
    seed_number = seed
    current_num = seed_number
    #print("Seed Number " + str(seed_number))
    for m in mappings:
        mapping = m[2]
        #print(current_num)
        #print(mapping)
        #print(mapping.keys())
        if str(current_num) in mapping:
            #print("Found Match " + str(mapping[str(current_num)]))
            current_num = mapping[str(current_num)]
            #print(current_num)
        else:
            #print("No Match Found")
            current_num = current_num
    return current_num

def get_lowest_value(l: [int]):
    #32 bit largest number - should cover most cases - check here if debugging
    lowest = 12147483647
    for i in l:
        if i < lowest:
            lowest = i
    return lowest
        

def get_location_from_seeds(seed_data, mappings):
    locations = []
    for s in seed_data['seeds']:
        locations.append(int(get_location_from_seed(s, mappings)))
    return locations

data = read_from_txt("data.txt")
seed_data, clean_data = clean_raw_data(data)
mappings = create_mappings(clean_data)
locations = get_location_from_seeds(seed_data, mappings)
answer = get_lowest_value(locations)
print(answer)