try:
    file_name = input()#'./takovata-access.log'


    def return_part_string(line, start_string, end_string):
        url_start_index = line.rfind(start_string)
        temp_string_array = None
        if url_start_index > -1:
            temp_string_array = data_in_line[url_start_index:].split(end_string)

        return temp_string_array[1]

    data = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            data_in_line = line.strip()

            url = return_part_string(data_in_line, 'url="', '"')
            if '?' in url:
                temp_url = url.split('?')
                url = temp_url[0]

            response_time = float(return_part_string(data_in_line, 'resp_t="', '"'))

            if url.endswith('/ws/'):
                continue
            else:
                if url not in data:
                    data[url] = []

                data[url].append(response_time)

    longest_mid_time = 0.0
    url_for_longets_mid_time = None
    for key, value in data.items():
        time = sum(value) / len(value)
        if time > longest_mid_time:
            longest_mid_time = time
            url_for_longets_mid_time = key

    print(url_for_longets_mid_time)
    print("{0:.3f}".format(longest_mid_time))

except:
    print('INVALID INPUT')