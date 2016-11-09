import math

try:
    dm_moonshine = float(input())
    moonshine_cm = dm_moonshine * 1000.0

    file_name = './containers.txt'

    dict_barrels = {}
    with open(file_name, encoding='utf-8') as info:
        if not info:
            raise ValueError

        for line_info in info:
            line = line_info.strip()
            if not line:
                continue

            data = line.split(',')
            barrel = data[0]
            r = float(data[1])
            h = float(data[2])

            if barrel in dict_barrels:
                continue

            else:
                dict_barrels[barrel] = [r, h]

    #π * r^2 * h
    smallest_container = float('inf')
    best_container = None
    for key, value in dict_barrels.items():
        cm3 = math.pi * value[0]**2 * value[1]
        if cm3 >= moonshine_cm and cm3 <= smallest_container:
            smallest_container = cm3
            best_container = key

    if best_container:
        print(best_container)

    else:
        print('NO SUITABLE CONTAINER')

except:
    print('INVALID INPUT')
