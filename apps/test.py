import unittest
from apps import constants
from apps.beverages import Tea, Coffee
from apps.ingredients import Sugar, Cream, Cinnamon


class TestValue(unittest.TestCase):

    def test_value_sugar(self):
        value = constants.Value.SUGAR
        sugar = Sugar()
        self.assertEqual(value, sugar.value)

    def test_value_cream(self):
        value = constants.Value.CREAM
        cream = Cream()
        self.assertEqual(value, cream.value)

    def test_value_cinnamon(self):
        value = constants.Value.CINNAMON
        cinnamon = Cinnamon()
        self.assertEqual(value, cinnamon.value)

    def test_value_tea(self):
        value = constants.Value.TEA
        tea = Tea()
        self.assertEqual(value, tea.value)

    def test_value_coffee(self):
        value = constants.Value.COFFEE
        coffee = Coffee()
        self.assertEqual(value, coffee.value)

    def test_tea_list_ingredients_assert(self):
        beverage = Tea()
        with self.assertRaises(AssertionError):
            beverage.add(Sugar(), 5)

    def test_coffee_list_ingredients_assert(self):
        beverage = Coffee()
        with self.assertRaises(AssertionError):
            beverage.add(Cream(), 'sas')

    def test_tea_total_value(self):
        beverage = Tea()
        res = constants.Value.TEA
        beverage.add(Sugar(), Cream(), Cinnamon())
        res += constants.Value.SUGAR + constants.Value.CREAM + constants.Value.CINNAMON
        self.assertEqual(res, beverage.total_value())

    def test_coffee_total_value(self):
        beverage = Coffee()
        res = constants.Value.COFFEE
        beverage.add(Sugar(), Cream(), Cinnamon())
        res += constants.Value.SUGAR + constants.Value.CREAM + constants.Value.CINNAMON
        self.assertEqual(res, beverage.total_value())
