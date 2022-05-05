from logging import warning
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from carfactory import CarFactory
from datetime import datetime

class setUp(unittest.TestCase):

# Test Batteries
    # Change last service date and self.assert statement as needed
    def test_calliope_battery(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    
    def test_glissade_battery(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_palindrome_battery(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(current_date,last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_rorschach_battery(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_thovex_battery(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())


# Test Engines
    def test_calliope_engine(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date,last_service_date,current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_engine(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date,last_service_date,current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_palindrome_engine(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(current_date,last_service_date,warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_rorschach_engine(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date,last_service_date,current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_engine(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date,last_service_date,current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    
    unittest.main()