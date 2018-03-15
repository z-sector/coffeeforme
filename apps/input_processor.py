"""
Module for python compatibility when using functions raw_input and input
"""
my_input = None
try:
    my_input = raw_input
except NameError:
    my_input = input
