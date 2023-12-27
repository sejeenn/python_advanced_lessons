from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired
import logging

app = Flask(__name__)
logger = logging.getLogger("divider")


class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])


@app.route("/divide/", methods=["POST"])
def divide():
    form = DivideForm()
    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        logger.debug(f"форма валидна, а={a}, b={b}")
        return f"a / b = {a / b:.2f}"
    logger.error(f"форма не валидна, error={form.errors}")
    return f"Неверный запрос", 400


@app.errorhandler(ZeroDivisionError)
def handle_exception(obj_err: ZeroDivisionError):
    logger.exception("На ноль делить нелья!", exc_info=obj_err)
    return "На ноль делить нельзя", 400


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Сервер деления чисел стартовал!")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)


