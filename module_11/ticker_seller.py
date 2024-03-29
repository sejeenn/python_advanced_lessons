import logging
import time
import threading
import random


TOTAL_TICKET = 10

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKET
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKET <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKET -= 1
                logger.info(f"{self.getName()} sold one; {TOTAL_TICKET} left")
        logger.info(f"Seller {self.getName()} sold {self.tickets_sold} tickets")

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore()
    sellers = []
    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == "__main__":
    main()

