import hashlib
import getpass
# def create_password():
#     password = input("Введите ваш пароль: ")
#     hash_obj = hashlib.md5(password.encode())
#     print(hash_obj.hexdigest())


def input_and_check_password():
    password: str = getpass.getpass()
    if not password:
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode('latin-1'))
        if hasher.hexdigest() == "d8578edf8458ce06fbc5bb76a58c5ca4":
            return True
    except ValueError:
        pass
    return False


if __name__ == '__main__':
    # создание хешированного пароля
    # create_password()
    count_number: int = 3
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    exit(1)

