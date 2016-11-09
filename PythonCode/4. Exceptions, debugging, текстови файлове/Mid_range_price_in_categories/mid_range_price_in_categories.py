catalog = {
    'infant': [],
    'kid': [],
    'men': [],
    'unisex': [],
    'woman': []
}

with open('C:/Users/Admin/Desktop/PythonFiles/catalog_sample.csv') as file:
    for line in file:
        lineArray = line.strip().split(',')
        customer_type = str(lineArray[-2]).lower()
        price = float(lineArray[-1].strip('"'))

        if customer_type in catalog:
            catalog[customer_type].append(price)

for key, value in catalog.items():
    result = sum(catalog[key]) / len(catalog[key])
    print(key + ": {0:.2f} lv.".format(result))