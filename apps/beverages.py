from ingredients import Ingredient
from mylogger import *
import constants



class Beverage(object):
    """
    Class create beverages
    """

    def __init__(self):
        """
        Constructor for object bevetage
        """
        self._value = 0
        self.list_ingredients = []

    @property
    def value(self):
        """
        Value of the ingredient
        :rtype: float

        """
        return self._value

    def add(self, *items):
        """
        Adding ingredients to the list
        :param items:
        :type items:
        """
        for item in items:
            if not isinstance(item, Ingredient):
                logger.error(
                    "Object {} is not added to the {}".format(item.__class__.__name__, self.__class__.__name__))
                assert isinstance(item, Ingredient)
            self.list_ingredients.append(item)
            logger.info("Ingredient {} is added to the {}".format(item.__class__.__name__, self.__class__.__name__))

    def total_value(self):
        """
        Determines the total value of the beverage
        :rtype: float
        """
        summ = self.value + sum([_.value for _ in self.list_ingredients])
        return float(summ)


class Tea(Beverage):
    """
        Class create tea
    """

    def __init__(self):
        """
        Constructor for object tea
        """
        super(Tea, self).__init__()
        self._value = constants.Value.TEA
        if not isinstance(self._value, (int, float)):
            logger.error("{} object was not created with value {}".format(self.__class__.__name__, self._value))
            raise ValueError("Value {} must be a numeric".format(self.__class__.__name__))
        logger.info("Created object {} with {}".format(self.__class__.__name__, self._value))


class Coffee(Beverage):
    """
        Class create coffee
    """

    def __init__(self):
        """
        Constructor for object coffee
        """
        super(Coffee, self).__init__()
        self._value = constants.Value.COFFEE
        if not isinstance(self._value, (int, float)):
            logger.error("{} object was not created with value {}".format(self.__class__.__name__, self._value))
            raise ValueError("Value {} must be a numeric".format(self.__class__.__name__))
        logger.info("Created object {} with {}".format(self.__class__.__name__, self._value))
