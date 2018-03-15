This is a command-line utility for use by sellers and managers of the company CoffeeForMe
Arguments of the utility are entered through the command line, also it is possible through the interactive mode

File for downloading the script - coffeforme.py


Options:
  --help, -h          Reference

Possible commands:
  Commands that must be the first parameter coffeforme

  {salesman,manager}
    salesman          Running in the mode "Salesman!"
    manager           Running in the mode "Manager!"
-----------------------------------------------------
MODE SALESMAN

usage: coffeforme salesman [--names NAME [NAME ...]]
                           [--beverage BEVERAGE TYPE]
                           [--ingredients INGREDIENTS [INGREDIENTS ...]]
                           [--price [PRICE]] [--save [SAVE]] [--help]

Running in the mode "Salesman!". In this mode, the program by type of drink
and ingredients determines the total cost of the drink.

Options:
  --names NAME [NAME ...], -n NAME [NAME ...]
                        User name
  --beverage BEVERAGE TYPE, -b BEVERAGE TYPE
                        Beverage type ['tea', 'coffee']
  --ingredients INGREDIENTS [INGREDIENTS ...], -i INGREDIENTS [INGREDIENTS ...]
                        Additional beverage ingredients ['sugar', 'cream',
                        'cinnamon']
  --price [PRICE], -p [PRICE]
                        Get a preliminary total price for a drink
  --save [SAVE], -s [SAVE]
                        Creates a check in the <bill> file (./bill/), saves the data to
                        the <sales.csv> file (./file/) and to the <salesdb> database (./database/)
  --help, -h            Reference


-----------------------------------------------------
MODE MANAGER

usage: coffeforme manager [--names NAME [NAME ...]] [--help]

Running in the mode "Salesman!". This mode provides a summary of all sales
records.

Options:
  --names NAME [NAME ...], -n NAME [NAME ...]
                        User name
  --help, -h            Reference
-----------------------------------------------------
LOGGING

Rotate logs is located in the folder <log>

-----------------------------------------------------
BILL

In the Bill file, the data on the last sale of the drink

-----------------------------------------------------
CSV and DATABASE

Information is stored in the following form:
USER NAME;beverage;ingredient, ingredien;total_value