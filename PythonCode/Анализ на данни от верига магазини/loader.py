import iso8601
import sys
from datetime import datetime, timezone
from decimal import Decimal
from product import Product
from database import Database as Data


def main():
    # if len(sys.argv) < 3:
    #     print('INVALID INPUT')
    # else:
    #     catalog_file = sys.argv[1]
    #     sales_file = sys.argv[2]
    #     print(catalog_file)
    #     print(sales_file)

    catalog_file = 'C:/Users/Admin/Desktop/PythonFiles/sales-analysis/catalog.csv'
    sales_file = 'C:/Users/Admin/Desktop/PythonFiles/sales-analysis/sales-10K.csv'

    load_products_data(catalog_file, sales_file)

    result_general_information = general_info(sales_file)
    print(result_general_information)

    result_categories = sales_by_categories()
    print(result_categories)


def load_products_data(catalog_file, sales_file):
    Data.catalog = {}
    Data.product_data = {}
    with open(catalog_file, encoding='utf-8') as file:
        for line in file:
            line_data = line.strip().split(',')
            product_info = [item.strip('"') for item in line_data]
            Data.catalog[product_info[0]] = product_info[-3]

    with open(sales_file, encoding='utf-8') as file:
        for line in file:
            line_data = line.strip().split(',')
            product_info = [item.strip('"') for item in line_data]
            if product_info[0] in Data.catalog:
                price = Decimal(product_info[4])
                date_sold = iso8601.parse_date(product_info[3])
                country_sold = product_info[1]
                city_sold = product_info[2]

                if product_info[0] not in Data.product_data:
                    Data.product_data[product_info[0]] = []

                Data.product_data[product_info[0]].append(
                        Product(
                                product_id=product_info[0],
                                product_type=Data.catalog[product_info[0]],
                                price=price,
                                date_sold=date_sold,
                                country_sold=country_sold,
                                city_sold=city_sold
                        ))
            else:
                print('Product from sales with id {} not added in catalog of products!'.format(product_info[0]))


def general_info(sales_file):
    sales_count = 0
    with open(sales_file, encoding='utf-8') as file:
        for line in file:
            sales_count += 1

    sales_price_amount = 0
    dates = []
    for key, value in Data.product_data.items():
        for item in value:
            sales_price_amount += item.price
            dates.append(item.data_sold.astimezone(timezone.utc))

    data_start_time = min(dates)
    data_end_time = max(dates)

    info = """    Обобщение
    ---------
        Общ брой продажби: {sales}
        Общо сума продажби: {all_sales_sum} €
        Средна цена на продажба: {mid_range_price} €
        Начало на период на данните: {start_date}
        Край на период на данните: {end_date}
        """.format(
            sales=sales_count,
            all_sales_sum=sales_price_amount,
            mid_range_price=sales_price_amount / sales_count,
            start_date=data_start_time,
            end_date=data_end_time
    )

    return info


def sales_by_categories():
    jackets_price = Decimal(0.0)
    shoes_price = Decimal(0.0)
    suits_price = Decimal(0.0)
    balls_price = Decimal(0.0)
    t_shirts_price = Decimal(0.0)
    for key, value in Data.product_data.items():
        for item in value:
            if item.type == "JACKETS":
                jackets_price += item.price
            if item.type == "SHOES":
                shoes_price += item.price
            if item.type == "SUITS":
                suits_price += item.price
            if item.type == "BALLS":
                balls_price += item.price
            if item.type == "T-SHIRTS":
                t_shirts_price += item.price

    all_prices = {
        jackets_price: "JACKETS",
        shoes_price: "SHOES",
        suits_price: "SUITS",
        balls_price: "BALLS",
        t_shirts_price: "T-SHIRTS",
    }

    base_message = """    Сума на продажби по категории (top 5)
    -----------------------------"""
    jackets = "\n        Якета            : {} {:.2f} €".format(get_stars(jackets_price, all_prices), jackets_price)
    shoes = "\n        Обувки за футбол : {} {:.2f} €".format(get_stars(shoes_price, all_prices), shoes_price)
    suits = "\n        Екипи            : {} {:.2f} €".format(get_stars(suits_price, all_prices), suits_price)
    balls = "\n        Топки            : {} {:.2f} €".format(get_stars(balls_price, all_prices), balls_price)
    t_shirts = "\n        T-SHIRTS         : {} {:.2f} €".format(get_stars(t_shirts_price, all_prices), t_shirts_price)

    info = base_message
    sorted_prices = [p for p in all_prices.keys()]
    sorted_prices.sort(reverse=True)
    for price in sorted_prices:
        if all_prices[price] == "JACKETS":
            info += jackets
        if all_prices[price] == "SHOES":
            info += shoes
        if all_prices[price] == "SUITS":
           info += suits
        if all_prices[price] == "BALLS":
            info += balls
        if all_prices[price] == "T-SHIRTS":
            info += t_shirts

    return info


def get_stars(price, data_values):
    max_value = max(data_values.keys())
    max_chart_width = 40
    value_per_star = max_value / max_chart_width

    return "".join(['*' * int(price / value_per_star)])


if __name__ == "__main__":
    sys.exit(main())