
class Car:
    def __init__(self, brand, year, model, engine, color,  price=0, is_electric=False):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.price = price
        self.is_electric = is_electric
        self.year = year
        self.color = color

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_engine(self):
        return self.engine

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_price(self):
        if self.price > 0:
            return self.price
        else:
            raise ValueError("Price should be greather than 0")

    def get_is_electric(self):
        if self.engine == "electric":
            return True
        else:
            return False

    def get_is_new_car(self):
        if self.year > 2015:
            return True
        else:
            return False

    def get_is_black(self):
        if self.color == "black":
            return True
        else:
            return False

    def get_is_black_and_electric(self):
        if self.color == "black" and self.engine == "electric":
            return True
        else:
            return False





