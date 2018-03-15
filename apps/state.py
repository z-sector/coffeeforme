import os.path
from beverages import Tea, Coffee
from ingredients import Sugar, Cream, Cinnamon
import csv
import os.path
import sqlite3
from mylogger import *
import sys

COMMAND_SQL_CREATE_TABLE = '''Create TABLE SALES (USER TEXT, BEVERAGE TEXT, INGREDIENTS TEXT, VALUE REAL)'''
COMMAND_SQL_INSERT = '''INSERT INTO SALES VALUES (?, ?, ?, ?)'''
COMMAND_SQL_SELECT = '''SELECT * FROM SALES'''



class State(object):
    """
    Class for saving  and loading data
    """

    def __init__(self, name):
        self._name = name
        logger.info("Created object {} with {}".format(self.__class__.__name__, self._name))

    @property
    def name(self):
        return self._name

    def load_state(self, mode='db'):
        """
        Function for loading data
        :param mode:
        :type str:
        :return: result
        :rtype: list
        """
        logger.info("Function load_state is started")
        result = {}
        if mode == 'db':
            logger.info('Reading data from a database')
            try:
                path = os.path.abspath('./database/' + self.name + 'db')
                conn = sqlite3.connect(path)
                with conn:
                    cur = conn.cursor()
                    for row in cur.execute(COMMAND_SQL_SELECT):
                        if not row[0] in result:
                            result[row[0]] = [float(row[3]), 1]
                        else:
                            result[row[0]][0] += float(row[3])
                            result[row[0]][1] += 1
            except sqlite3.OperationalError:
                logger.error(
                    'Unable to open database file: {}'.format([_ for _ in os.walk(os.path.abspath('./database/'))]))
                sys.exit(1)
        else:
            logger.info('Reading data from a file(csv)')
            try:
                path = os.path.abspath('./file/' + self.name + '.csv')
                with open(path, 'r') as file_:
                    for line in file_:
                        lst = line.strip().split(';')
                        if lst[0] == 'user':
                            continue
                        if not lst[0] in result:
                            result[lst[0]] = [float(lst[3]), 1]
                        else:
                            result[lst[0]][0] += float(lst[3])
                            result[lst[0]][1] += 1
            except IOError:
                logger.error('No such file or directory: {}'.format(path))
                logger.info('----------COMPLETED----------')
                sys.exit(1)

        logger.info('Function load_state completed')

        return result

    def save_state(self, beverage, user, arg_beverage, ingredients):
        """
        Function for saving data
        :param beverage:
        :type beverage:
        :param user:
        :type str:
        :param arg_beverage:
        :type str:
        :param ingredients:
        :type list:
        """
        logger.info("Function save_state is started")
        if arg_beverage == 'tea':
            beverage = Tea()
        elif arg_beverage == 'coffee':
            beverage = Coffee()
        for ingredient in ingredients:
            if ingredient == 'sugar':
                add_ingredient = Sugar()
            elif ingredient == 'cream':
                add_ingredient = Cream()
            elif ingredient == 'cinnamon':
                add_ingredient = Cinnamon()
            beverage.add(add_ingredient)

        path = os.path.abspath('./file')

        try:
            os.mkdir(path)
            logger.info('Created folder file')
        except OSError:
            pass
        with open(os.path.abspath('./file/' + self.name + '.csv'), "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=';', lineterminator="\n")
            writer.writerow([user, arg_beverage, ', '.join(ingredients), beverage.total_value()])
            logger.info('Information saved to file:{}'.format(
                [user, arg_beverage, ', '.join(ingredients), beverage.total_value()]))
        path = os.path.abspath('./bill')
        try:
            os.mkdir(path)
            logger.info('Created folder bill')
        except OSError:
            pass
        with open(os.path.abspath('./bill/bill'), "w") as file_:
            file_.write("User:\n" + user + '\n')
            file_.write("Beverage:\n" + beverage.__class__.__name__ + ' - ' + str(beverage.value) + '\n')
            file_.write("Ingredient:\n")
            for ingredient in beverage.list_ingredients:
                file_.write(ingredient.__class__.__name__ + ' - ' + str(ingredient.value) + '\n')
            if beverage.list_ingredients == []:
                file_.write('- \n')
            file_.write("Total purchase price:\n" + str(beverage.total_value()))
            logger.info('Information saved to file <bill>')

        path = os.path.abspath('./database')
        try:
            os.mkdir(path)
            logger.info('Created folder database')
        except OSError:
            pass
        conn = sqlite3.connect(os.path.abspath('./database/' + self.name + 'db'))
        with conn:
            cur = conn.cursor()
            try:
                cur.execute(COMMAND_SQL_CREATE_TABLE)
            except sqlite3.OperationalError:
                pass
            cur.execute(COMMAND_SQL_INSERT,
                        (user, arg_beverage, ', '.join(ingredients), beverage.total_value()))
            logger.info('Information saved to database:{}'.format(
                [user, arg_beverage, ', '.join(ingredients), beverage.total_value()]))

        logger.info('Function save_state completed')
