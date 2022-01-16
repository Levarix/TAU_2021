import unittest
from src.main import isOdd, encryptPassword, decryptPassword, Car

class IsOddTestCase(unittest.TestCase):
    def is_odd_return_true(self):
        assert isOdd(5) == True

    def is_odd_return_false(self):
        assert isOdd(4) == False


class CipherTestCase(unittest.TestCase):
    def encrypt_return_encrypted(self):
        assert encryptPassword("Test", "Password") == "935S952S966S967"

    def decrypt_return_decrypted(self):
        assert decryptPassword("935S952S966S967", "Password") == "Test"

class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.electric_car = Car(brand="Tesla", model="X", color="gray", engine="electric", price=50000, year=2020)
        self.diesel_car = Car(brand="Alfa Romeo", model="159", color="black", engine="diesel", price=-200, year=2006)

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

    def test_is_new_car_returns_true(self):
        self.assertTrue(self.electric_car.get_is_new_car())

    def test_is_new_car_returns_false(self):
        self.assertFalse(self.diesel_car.get_is_new_car())

    def test_is_black_car_returns_true(self):
        self.assertTrue(self.diesel_car.get_is_black())

    def test_is_black_car_returns_false(self):
        self.assertFalse(self.electric_car.get_is_black())

    def test_get_year_return_year(self):
        self.assertEqual(self.electric_car.get_year(), 2020)

    def test_get_color_return_color(self):
        self.assertEqual(self.diesel_car.get_color(), "black")

    def test_get_is_black_and_electric_return_False(self):
        self.assertTrue(self.diesel_car.get_is_black_and_electric())


if __name__ == '__main__':
    unittest.main()