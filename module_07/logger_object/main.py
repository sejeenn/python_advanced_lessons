import logging
import flask

from http_utils import get_ip_address
from subprocess_utils import get_kernel_version


logging.basicConfig(level="DEBUG")
root_logger = logging.getLogger()
main = logging.getLogger('main')
main.setLevel("INFO")
utils = logging.getLogger('utils')
utils.setLevel("DEBUG")

app = flask.Flask(__name__)


@app.route("/get_system_info")
def get_system_info():
    print(root_logger)
    print(main)
    print(utils)
    main.info('Start working')
    ip = get_ip_address()
    kernel = get_kernel_version()
    return f"<p>{ip}</p><p>{kernel}</p>"


if __name__ == '__main__':
    app.run(debug=True)
