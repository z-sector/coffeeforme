from apps import constants
from mylogger import *



class Ingredient(object):
    """
    Class create ingredients
    """

    def __init__(self):
        """
        Constructor for object ingredient
        """
        self._value = None

    @property
    def value(self):
        """
        Value of the ingredient
        :rtype: float

        """
        return self._value


class Sugar(Ingredient):
    """
    Class create sugar
    """

    def __init__(self, value=constants.Value.SUGAR):
        """
        Constructor for object sugar
        :param value:
        :type value:
        """
        super(Sugar, self).__init__()
        if not isinstance(value, (int, float)):
            logger.error("{} object was not created with value {}".format(self.__class__.__name__, value))
            raise ValueError("Value {} must be a numeric".format(self.__class__.__name__))
        self._value = float(value)
        logger.info("Created object {} with {}".format(self.__class__.__name__, self._value))


class Cream(Ingredient):
    """
    Class create cream
    """

    def __init__(self, value=constants.Value.CREAM):
        """
        Constructor for object cream
        :param value:
        :type value:
        """
        super(Cream, self).__init__()
        if not isinstance(value, (int, float)):
            logger.error("{} object was not created with value {}".format(self.__class__.__name__, value))
            raise ValueError("Value {} must be a numeric".format(self.__class__.__name__))
        self._value = float(value)
        logger.info("Created object {} with {}".format(self.__class__.__name__, self._value))


class Cinnamon(Ingredient):
    """
    Class create cinnamon
    """

    def __init__(self, value=constants.Value.CINNAMON):
        """
        Constructor for object cinnamon
        :param value:
        :type value:
        """
        super(Cinnamon, self).__init__()
        if not isinstance(value, (int, float)):
            logger.error("{} object was not created with value {}".format(self.__class__.__name__, value))
            raise ValueError("Value {} must be a numeric".format(self.__class__.__name__))
        self._value = float(value)
        logger.info("Created object {} with {}".format(self.__class__.__name__, self._value))
