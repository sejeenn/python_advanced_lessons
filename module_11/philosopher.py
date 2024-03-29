import logging
import threading
import random
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    def __int__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            logger.info(f"Philosopher {self.getName()} start thinking")
            time.sleep(random.randint(1, 5))
            logger.info(f"Philosopher {self.getName()} is hungry")
            self.left_fork.acquire()
            time.sleep(random.randint(1, 5))
            logger.info(f"Philosopher {self.getName()} acquired left fork")
            try:
                self.right_fork.acquire()
                logger.info(f"Philosopher {self.getName()} acquired right fork")
                self.dining()
            finally:
                self.left_fork.release()
                self.right_fork.release()

    def dining(self):
        logger.info(f"Philosopher {self.getName()} start eating")
        time.sleep(random.randint(1, 5))
        logger.info(f"Philosopher {self.getName()} finishes eating and leaves to think")


def main():
    forks = [threading.Lock for n in range(5)]
    philosophers = [
        Philosopher(forks[i % 5], forks[(i * 1) % 5])
        for i in range(5)
    ]
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(200)
    Philosopher.running = False
    logger.info("Now we're finishing")


if __name__ == '__main__':
    main()
