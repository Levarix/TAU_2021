class Car:
    def __init__(self, brand, model, engine, price=0, is_electric=False):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.price = price
        self.is_electric = is_electric

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_engine(self):
        return self.engine

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