from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)


class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])


@app.route("/divide/", methods=["POST"])
def divide():
    form = DivideForm()
    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        print('a, b: ', a, b)
        return f"a / b = {a / b:.2f}"
    return f"Неверный запрос", 400


@app.errorhandler(ZeroDivisionError)
def handle_exception(obj_err: ZeroDivisionError):
    return "На ноль делить нельзя", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)


