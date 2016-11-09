try:
    key = int(input())
    message = input()


    def symbol_set_number(symbol_to_number):
        number = symbol_to_number

        if number > 90:
            temp = number - 90
            number = 65 + temp
            if number < 91:
                return number - 1
            else:
                temp_result = symbol_set_number(number)


    for symbol in message:
        symbol_number = ord(symbol)
        if symbol_number >= 65 and symbol_number <= 90:
            symbol_number += key
            if symbol_number > 90:
                symbol_number = symbol_set_number(symbol_number)

        coded_symbol = chr(symbol_number)
        print(coded_symbol, end="")

except:
    print('INVALID INPUT')


