catalog = list()
with open('C:/Users/Admin/Desktop/PythonFiles/catalog_sample.csv') as file:
    for line in file:
        lineArray = line.strip().split(',')
        price = float(lineArray[-1].strip('"'))
        catalog.append(price)

result = sum(catalog) / len(catalog)
print("{0:.2f}".format(result))