try:
    width = float(input())
    high = float(input())
    depth = float(input())
    packages_file_name = input()

    box_dimensions = sorted([width, high, depth])


    with open(packages_file_name, encoding='utf-8') as packages:
        for line in packages:
            line_data = line.strip().split(',')

            current_box_dimensions = \
                sorted([float(line_data[1]), float(line_data[2]), float(line_data[3])])

            if box_dimensions[0] > current_box_dimensions[0] and \
                            box_dimensions[1] > current_box_dimensions[1] and \
                            box_dimensions[2] > current_box_dimensions[2]:
                print(line_data[0])

except:
    print('INVALID INPUT')
