from apps.my_argparse import *
from apps.mylogger import *


if __name__ == '__main__':
    logger.info('----------STARTING----------')
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        logger.info('----------COMPLETED----------')
        sys.exit(1)
    elif not sys.argv[1] in ['manager', 'salesman']:
        parser.print_help()
        logger.info('----------COMPLETED----------')
        sys.exit(1)
    else:
        namespace = parser.parse_args()

    if namespace.command == "manager":
        run_manager(namespace)
    elif namespace.command == "salesman":
        run_salesman(namespace)
    logger.info('----------COMPLETED----------')
