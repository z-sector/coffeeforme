from constants import BeverageId, IngredientId
from state import State
from beverages import Tea, Coffee
from ingredients import Sugar, Cream, Cinnamon
from input_processor import *
from mylogger import *
import argparse
import sys



def create_parser():
    logger.info("Function create_parser is started")
    # Create a parser class
    parser = argparse.ArgumentParser(prog='coffeforme',
                                     description='''This is a command-line utility for use by sellers and managers 
                                     of the company CoffeeForMe''',
                                     add_help=False)

    # Create a parameter group for the parent parser
    parent_group = parser.add_argument_group(title='Options')
    parent_group.add_argument('--help', '-h', action='help', help='Reference')

    # Create a group of sub-parsers
    subparsers = parser.add_subparsers(dest='command', title='Possible commands',
                                       description='Commands that must be the first parameter %(prog)s')

    # Create a parser for the command Salesman
    salesman_parser = subparsers.add_parser('salesman',
                                            add_help=False,
                                            help='Running in the mode "Salesman!"',
                                            description='''Running in the mode "Salesman!".
    In this mode, the program by type of drink and ingredients determines the total cost of the drink.''')
    # Create a new group of parameters
    salesman_group = salesman_parser.add_argument_group(title='Options')
    # Adding options
    salesman_group.add_argument('--names', '-n', nargs='+', type=str,
                                help='User name',
                                metavar='NAME')
    salesman_group.add_argument('--beverage', '-b', help='Beverage type {}'.format([_.name for _ in BeverageId]),
                                metavar='BEVERAGE TYPE',
                                choices=[_.name for _ in BeverageId])
    salesman_group.add_argument('--ingredients', '-i',
                                help='Additional beverage ingredients {}'.format([_.name for _ in IngredientId]),
                                metavar='INGREDIENTS', nargs='+', type=str,
                                choices=[_.name for _ in IngredientId])
    salesman_group.add_argument('--price', '-p', help='Get a preliminary total price for a drink', metavar='PRICE',
                                type=str, const='y', nargs='?')
    salesman_group.add_argument('--save', '-s',
                                help='Creates a check in the <bill> file, saves the data to the <sales> file and to the <wre> database',
                                metavar='SAVE', type=str, const='y', nargs='?')
    salesman_group.add_argument('--help', '-h', action='help', help='Reference')
    # Create a parser for the command Manager
    manager_parser = subparsers.add_parser('manager',
                                           add_help=False,
                                           help='Running in the mode "Manager!"',
                                           description='''Running in the mode "Salesman!". 
                                           This mode provides a summary of all sales records.''')

    # Create a new group of parameters
    manager_group = manager_parser.add_argument_group(title='Options')

    # Adding options
    manager_group.add_argument('--names', '-n', nargs='+', type=str,
                               help='User name',
                               metavar='NAME')
    manager_group.add_argument('--help', '-h', action='help', help='Reference')

    logger.info('Function create_parser completed')

    return parser


def run_manager(namespace):
    """

    :param namespace:
    :type namespace:
    :return:
    :rtype:
    """
    logger.info("Function run_manager is started")

    if namespace.names is None:
        logger.info("Username entered through interactive mode")
        while True:
            name = my_input("Enter the user name (enter 'q' to exit)!")
            if len(name) == 0:
                logger.warning('You have not entered a user name, try again')
            elif name.lower() == 'q':
                logger.info('----------COMPLETED----------')
                sys.exit(1)
            else:
                break
    else:
        name = namespace.names

    shop = State('sales')
    result = shop.load_state()
    s_1 = 'Seler name'
    s_2 = 'Number of sales'
    s_3 = 'Total Value'
    logger.warning('{:<16}'.format(s_1) + '|' + '    {:<16}'.format(s_2) + '|' + '    {:<12}'.format(s_3))
    for key in result:
        logger.warning('{:<16}'.format(key) + '|' + '    {:<16}'.format(result[key][1]) + '|' + '    {:<12}'.format(
            result[key][0]))
    logger.warning("The program is completed!")

    logger.info('Function run_manager completed')


def run_salesman(namespace):
    """

    :param namespace:
    :type namespace:
    """
    logger.info("Function run_salesman is started")
    if namespace.names is None:
        logger.info("Username entered through interactive mode")
        while True:
            name = my_input("Enter the user name (enter 'q' to exit):").upper().strip()
            if len(name) == 0:
                logger.warning('You have not entered a user name, try again')
            elif name == 'Q':
                logger.info('----------COMPLETED----------')
                sys.exit(1)
            else:
                break
    else:
        name = ' '.join(namespace.names).upper().strip()

    if namespace.beverage is None:
        logger.info("Beverage entered through interactive mode")
        while True:
            beverage = my_input("Enter the beverage type (enter 'q' to exit):")
            if len(beverage) == 0:
                logger.warning('You have not entered a beverage, try again')
            elif beverage.lower() == 'q':
                logger.info('----------COMPLETED----------')
                sys.exit(1)
            elif not beverage in [_.name for _ in BeverageId]:
                logger.warning('There is no drink - {}'.format(beverage))
                logger.warning('The following drinks are available: {}'.format([_.name for _ in BeverageId]))
                logger.warning('try again')
            else:
                break
    else:
        beverage = namespace.beverage
        if not beverage in [_.name for _ in BeverageId]:
            logger.warning('There is no drink - {}'.format(beverage))
            logger.warning('The following drinks are available: {}'.format([_.name for _ in BeverageId]))
            logger.info('----------COMPLETED----------')
            sys.exit(1)

    if namespace.ingredients is None:
        logger.info("Ingredients entered through interactive mode")
        while True:
            ingredients = my_input("Enter the ingredients type (enter 'n' without ingredients or 'q' to exit):")
            if len(ingredients) == 0:
                logger.warning('You did not enter the ingredients, try again')
            elif ingredients.lower() == 'q':
                logger.info('----------COMPLETED----------')
                sys.exit(1)
            elif ingredients.lower() == 'n':
                ingredients = []
                break
            else:
                ingredients = ingredients.split()
                t = True
                for ingredient in ingredients:
                    if not ingredient in [_.name for _ in IngredientId]:
                        logger.error('There is no ingredient - {}'.format(ingredient))
                        t = False
                if t:
                    break
                else:
                    logger.warning('The following ingredients are available: {}'.format([_.name for _ in IngredientId]))
                    logger.warning('try again')
    else:
        ingredients = namespace.ingredients
        for ingredient in ingredients:
            if not ingredient in [_.name for _ in IngredientId]:
                logger.warning('There is no ingredient - {}'.format(ingredient))
                logger.warning('The following ingredients are available: {}'.format([_.name for _ in IngredientId]))
                logger.info('----------COMPLETED----------')
                sys.exit(1)

    if beverage == 'tea':
        result_bev = Tea()
    elif beverage == 'coffee':
        result_bev = Coffee()
    for ingredient in ingredients:
        if ingredient == 'sugar':
            add_ingredient = Sugar()
        elif ingredient == 'cream':
            add_ingredient = Cream()
        elif ingredient == 'cinnamon':
            add_ingredient = Cinnamon()
        result_bev.add(add_ingredient)

    if namespace.price not in ('y', 'n'):
        while True:
            logger.info("Pre-calculate entered through interactive mode")
            price = my_input("Pre-calculate the cost of a drink (y/n)?: ")
            if price == 'n':
                break
            elif price == 'y':
                break
            else:
                logger.error(
                    'The value (Pre-calculate the cost of a drink (y/n)?) is incorrectly entered - {}'.format(price))
                print("The value is incorrectly entered. It is necessary to enter y/n")
    else:
        price = namespace.price
    if price == 'y':
        if len(ingredients) == 0:
            logger.warning(
                "The total cost of the drink (without ingredients) - ".format(beverage, ', '.join(ingredients)) +
                str(result_bev.total_value()))
        else:
            logger.warning("The total cost of the drink ({} with {}) - ".format(beverage, ', '.join(ingredients)) +
                           str(result_bev.total_value()))
    logger.info('Pre-calculate the cost of a drink - {}'.format(price))

    if namespace.save not in ('y', 'n'):
        while True:
            logger.info("Create a check and save data entered through interactive mode")
            save = my_input("Create a check and save data (y/n)?: ")
            if save == 'n':
                break
            elif save == 'y':
                break
            else:
                logger.error(
                    'The value (Pre-calculate the cost of a drink (y/n)?) is incorrectly entered - {}'.format(price))
                logger.warning("The value is incorrectly entered. It is necessary to enter y/n")
    else:
        save = namespace.save
    if save == 'y':
        shop = State('sales')
        shop.save_state(result_bev, name, beverage, ingredients)
    logger.info('Create a check and save data - {}'.format(save))

    logger.info('Function run_salesman completed')

    logger.warning("The program is completed!")
