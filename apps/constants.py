from enum import Enum


class Value(object):
    """
    Class attributes return float

    Constants of the cost of drinks and ingredients
    :type : float
    """

    TEA = 1.0
    COFFEE = 2.0

    SUGAR = 0.3
    CREAM = 0.2
    CINNAMON = 0.1


class BeverageId(Enum):
    """
    Class of enumerated beverage objects
    """

    tea = 1
    coffee = 2


class IngredientId(Enum):
    """
    Class of enumerated ingredient objects
    """

    sugar = 1
    cream = 2
    cinnamon = 3
