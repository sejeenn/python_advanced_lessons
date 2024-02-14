import logging


root_logger = logging.getLogger()
module_logger = logging.getLogger('module_logger')
submodule_logger = logging.getLogger('module_logger.submodule_logger')


def main():
    print(root_logger)
    print(submodule_logger)
    print(submodule_logger.parent)


if __name__ == '__main__':
    main()
