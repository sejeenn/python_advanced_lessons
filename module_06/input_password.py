import hashlib
import getpass
import logging
# def create_password():
#     password = input("Введите ваш пароль: ")
#     hash_obj = hashlib.md5(password.encode())
#     print(hash_obj.hexdigest())

logger = logging.getLogger("password_checker")


def input_and_check_password():
    logger.debug("Начало input_and_check_password()")

    password: str = getpass.getpass()
    if not password:
        logger.warning('Пароль не может быть пустым!')
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode('latin-1'))
        if hasher.hexdigest() == "d8578edf8458ce06fbc5bb76a58c5ca4":
            logger.info('Пароль введен правильно!')
            return True
    except ValueError:
        pass
    logger.warning('Пароль введен неверно!')
    return False


if __name__ == '__main__':
    # создание хешированного пароля
    # create_password()

    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытаетесь зарегистрироваться в системе.")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попытки")
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error("Пользователь трижды ввел неправильный пароль!")
    exit(1)

