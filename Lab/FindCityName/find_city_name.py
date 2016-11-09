from decimal import Decimal

item_id = input()
file_name = input()

sales = []
with open(file_name, encoding='utf-8') as info:
        for line in info:
            line_data = line.strip().split(',')

            striped_list = []
            for item in line_data:
                striped_list.append(item.strip('"'))

            if striped_list[0] == item_id:
                sales.append(striped_list)

lowest_price = Decimal('Infinity')
town = None
for product_data in sales:
    if Decimal(product_data[-1]) < lowest_price:
        lowest_price = Decimal(product_data[-1])
        town = product_data[2]

print(town)


