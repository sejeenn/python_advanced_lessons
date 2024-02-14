import logging
import os.path
import time
import threading
import multiprocessing
import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = "https://loremflickr.com/400/400/cats"
OUT_PATH = "temp_mp/{}.jpeg"


def get_image(url: str, result_path: str):
    response = requests.get(url, timeout=(5, 5))
    if response.status_code != 200:
        return
    with open(result_path, 'wb') as out_file:
        out_file.write(response.content)


def load_images_sequential():
    start = time.time()
    procs = []
    for i in range(10):
        proc = multiprocessing.Process(
            target=get_image,
            args=(URL, OUT_PATH.format(i))
        )
        proc.start()
        procs.append(proc)
    for proc in procs:
        proc.join()

    logger.info('Done in {:.4}'.format(time.time() - start))


if __name__ == "__main__":
    if not os.path.exists('./temp_mp'):
        os.mkdir('./temp_mp')
    load_images_sequential()
