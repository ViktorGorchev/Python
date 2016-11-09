import iso8601
from datetime import *


file_name = './city‐temperature‐data.csv'

dict_temperatures = {}
with open(file_name, encoding='utf-8') as info:
    if not info:
        raise ValueError

    for line_info in info:
        line = line_info.strip()
        if not line:
            continue

        data = line.split(',')
        date_info = iso8601.parse_date(data[0])
        town = data[1]
        temperature = float(data[2])

        if town not in dict_temperatures:
            dict_temperatures[town] = []

        dict_temperatures[town].append(date_info)

temp_date = None
missing_dates_dict = {}

for key, value in dict_temperatures.items():
    if key not in missing_dates_dict:
        missing_dates_dict[key] = []

    value.sort()
    for date in value:
        if not temp_date:
            temp_date = date
            continue
        missing_date = timedelta(days=1)
        if date - temp_date > timedelta(days=1):
            while missing_date < date:
                missing_date = temp_date + timedelta(days=1)
                missing_dates_dict[key].append(missing_date)
                temp_date = missing_date



    temp_date = None

print(missing_dates_dict)
        # if date not in missing_dates_dict:
        #         missing_dates_dict[date]
        #
        # if not temp_date:
        #     temp_date = date
        #     continue
        #
        # if date - temp_date > timedelta(days=1):
        #
        #
        # temp_date = date




# keys_array_dates_sorted = [d for d in dict_temperatures]
# keys_array_dates_sorted.sort()
# missing_dates = []
# for index, sorted_key in enumerate(keys_array_dates_sorted):
#     if index == len(keys_array_dates_sorted) - 1:
#         continue
#     subtracted_dates = (keys_array_dates_sorted[index + 1] - keys_array_dates_sorted[index]) > timedelta(days=1)
#     if subtracted_dates:
#         missing_dates.append(sorted_key)







