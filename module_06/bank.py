import csv
from typing import Optional

from flask import Flask
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)


@app.route("/bank_api/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=",")

        for record in csv_reader:
            if int(record["id"]) == person_id:
                return record["name"]
        else:
            return "Person not found", 404 


@app.errorhandler(InternalServerError)
def handle_exception(object_err: InternalServerError):
    original: Optional[Exception] = getattr(object_err, "original_exception", None)

    if isinstance(original, FileNotFoundError):
        with open("invalid_error.log", "a") as file:
            file.write(
                f"Пытался получить доступ к {original.filename}. Exception info: {original.strerror}\n"
            )
    elif isinstance(original, OSError):
        with open("invalid_error.log", "a") as file:
            file.write(
                f"Нет доступа к записи Exception info: {original.strerror}\n"
            )
    return "Internal Server Error", 500


if __name__ == '__main__':
    app.run()
