import logging


logger = logging.getLogger()

print(logger)

logger.setLevel("DEBUG")

print(logger.level)


def main(name):
    logger.debug(f"Enter in the main() function name: name = {name}")


if __name__ == '__main__':
    main('Eugene')
    