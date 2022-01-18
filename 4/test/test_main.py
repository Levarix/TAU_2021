from unittest import TestCase
from unittest.mock import patch
import sys
sys.path.append('../src')
from Car import Car
from Welcome import Welcome

class CarTestCase(TestCase):

    @patch('Car.Car.get_is_electric', return_value=True)
    def test_get_is_electric_return_True(self, mock):
        car = Car(brand="Tesla", model="X", color="gray", engine="electric", price=50000, year=2020)
        returned_value = car.get_is_electric()
        mock.assert_called_once()
        self.assertTrue(returned_value)

    @patch('Car.Car.get_price', return_value=1500)
    def test_get_price_return_int(self, mock):
        car = Car(brand="Tesla", model="X", color="gray", engine="electric", price=1500, year=2020)
        returned_value = car.get_price()
        mock.assert_called_once()
        self.assertEqual(returned_value, 1500)

    @patch('Car.Car.get_is_black_and_electric', return_value=True)
    def test_get_is_black_and_electric_return_True(self, mock):
        car = Car(brand="Tesla", model="X", color="black", engine="electric", price=1500, year=2020)
        returned_value = car.get_is_black_and_electric()
        mock.assert_called_once()
        self.assertTrue(returned_value)

class WelcomeTestCase(TestCase):

    @patch('Welcome.Welcome.welcome', return_value="Witaj Andrzej!")
    def test_welcome_return_string_value(self, mock):
        welcome = Welcome(welcome="Witaj", name="Andrzej")
        returned_value = welcome.welcome()
        mock.assert_called_once()
        self.assertEqual(returned_value, "Witaj Andrzej!")

    @patch('Welcome.Welcome.welcome', return_value="Cześć Bezimienny!")
    def test_welcome_return_default_value(self, mock):
        welcome = Welcome()
        returned_value = welcome.welcome()
        mock.assert_called_once()
        self.assertEqual(returned_value, "Cześć Bezimienny!")

    @patch('Welcome.Welcome.welcome', return_value="Cześć 66!")
    def test_welcome_return_string_from_int_value(self, mock):
        welcome = Welcome()
        returned_value = welcome.welcome(name=66)
        mock.assert_called_once()
        self.assertEqual(returned_value, "Cześć 66!")
