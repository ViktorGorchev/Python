try:
    filename_exchange_rates = input()
    filename_amounts = input()

    rates_info = {}
    with open(filename_exchange_rates, encoding='utf-8') as rates:
        for line in rates:
            rates_data = line.strip().split()
            rates_info[rates_data[0]] = float(rates_data[1])

    with open(filename_amounts, encoding='utf-8') as amounts:
        for line in amounts:
            amounts_data = line.strip().split()
            if amounts_data[1] in rates_info:
                result = float(amounts_data[0]) / rates_info[amounts_data[1]]

                print("{:.2f}".format(result))

except:
    print('INVALID INPUT')



