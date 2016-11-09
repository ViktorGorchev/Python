class Product:

    def __init__(self, product_id, product_type, price=0, date_sold=None, country_sold=None, city_sold=None):
        self.id = product_id
        self.type = product_type
        self.price = price
        self.data_sold = date_sold
        self.country_sold = country_sold
        self.city_sold = city_sold

    def __repr__(self):
        return "Product: " + str(self.__dict__)