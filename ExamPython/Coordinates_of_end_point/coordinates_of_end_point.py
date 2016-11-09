try:
    file_name = input() #'./steps.txt'

    x_object_coordinates = 0.0
    y_object_coordinates = 0.0
    count = 0
    with open(file_name, encoding='utf-8') as info:
            for line in info:
                line_data = line.strip()
                if not line_data:
                    continue

                data = line_data.split()
                command = data[0]
                step = float(data[1])

                if command == 'right':
                    x_object_coordinates += step
                    count += 1

                elif command == 'left':
                    x_object_coordinates -= step
                    count += 1

                elif command == 'up':
                    y_object_coordinates += step
                    count += 1

                elif command == 'down':
                    y_object_coordinates -= step
                    count += 1

                else:
                    print('INVALID INPUT')

    if count == 0:
        print('INVALID INPUT')

    else:
        print('X {:.3f}'.format(x_object_coordinates))
        print('Y {:.3f}'.format(y_object_coordinates))

except:
    print('INVALID INPUT')


