file_name = input()

time_driving = 0.0
try:
    with open(file_name, encoding='utf-8') as info:
            for line in info:
                line_data = line.strip().split(',')

                start_point = float(line_data[0])
                end_point = float(line_data[1])
                speed = float(line_data[2])

                distance = end_point - start_point
                if start_point is not 0.0:
                    distance += 1

                time_driving += distance / speed

except:
    print('INVALID INPUT')

print("{0:.2f}".format(time_driving))