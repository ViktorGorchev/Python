try:
    temperature_difference = 4.0
    file_name = input()#'./fridge-temp.csv'

    list_of_data = []
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            data_in_line = line.strip().split(',')
            list_of_data.append(data_in_line)

    list_of_data.sort()

    temp_temperature = 0.0
    for data in list_of_data:
        time = data[0]
        temperature = float(data[1])
        if temp_temperature > 0 and temperature - temp_temperature >= temperature_difference:
            print(time)

        temp_temperature = temperature

except:
    print('INVALID INPUT')