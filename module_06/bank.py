import csv
import logging
from typing import Optional

from flask import Flask
from werkzeug.exceptions import InternalServerError

app = Flask("bank")

logger = logging.getLogger(__name__)


@app.route("/bank_api/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
    logger.debug(f"Запрос пользователя id={person_id} из карточки {branch}")
    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, 'r') as file:
        logger.debug(f"Успешно открыта {branch} карточка")
        csv_reader = csv.DictReader(file, delimiter=",")

        for record in csv_reader:
            if int(record["id"]) == person_id:
                logger.debug(f"Успешно найдена запись пользователя с номером {person_id}")
                return record["name"]
        else:
            logger.debug(f"Пользователь с id={person_id} в карточке {branch} не найден.")
            return "Person not found", 404 


@app.errorhandler(InternalServerError)
def handle_exception(object_err: InternalServerError):
    logger.error("Handled uncaught exception")
    original: Optional[Exception] = getattr(object_err, "original_exception", None)

    if isinstance(original, FileNotFoundError):
        logger.error(
            f"Пытался получить доступ к файлу: {original.filename}. Exception error {original.strerror}"
        )

    elif isinstance(original, OSError):
        logger.error(
                f"Нет доступа к карточке Exception info: {original.strerror}\n"
            )
    return "Internal Server Error", 500


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename="banking.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    app.run()
