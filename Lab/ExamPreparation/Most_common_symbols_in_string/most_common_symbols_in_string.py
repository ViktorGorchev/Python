input_string = input()
if input_string is None:
    print('INVALID INPUT')
else:
    temp_string = None
    most_common_letter = None

    checked_list = []
    counter = 0
    temp_counter = 0
    for checked_letter in input_string:
        if checked_list == ' ':
            continue

        if checked_letter not in checked_list:

            for letter in input_string:
                if checked_letter == letter:
                    temp_counter += 1

        if temp_counter > counter:
            counter = temp_counter
            most_common_letter = checked_letter

        temp_counter = 0
        checked_list.append(checked_letter)

if len(checked_list) == 0:
    print('INVALID INPUT')
else:
    print(most_common_letter)