import unittest


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


class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.electric_car = Car(brand="Tesla", model="X", engine="electric", price=50000)
        self.diesel_car = Car(brand="Alfa Romeo", model="159", engine="diesel", price=-200)

    def tearDown(self):
        self.electric_car = None
        self.diesel_car = None

    def test_get_model_returns_model(self):
        self.assertEqual(self.electric_car.get_model(), "X")

    def test_get_engine_returns_engine(self):
        self.assertEqual(self.electric_car.get_engine(), "electric")

    def test_get_price_returns_price(self):
        self.assertEqual(self.electric_car.get_price(), 50000)

    def test_get_brand_returns_brand(self):
        self.assertEqual(self.electric_car.get_brand(), "Tesla")

    def test_get_price_raise_error(self):
        with self.assertRaises(ValueError):
            self.diesel_car.get_price()

    def test_get_is_electric_returns_true(self):
        self.assertTrue(self.electric_car.get_is_electric())

    def test_get_is_electric_returns_false(self):
        self.assertFalse(self.diesel_car.get_is_electric())

if __name__ == '__main__':
    unittest.main()
