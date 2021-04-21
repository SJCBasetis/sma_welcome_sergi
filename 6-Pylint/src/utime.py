"""
    Time utilities
"""

from datetime import datetime,time
from random import random

class MyTimer():
    """
        Object used to show times of execution

        Args:
            baseline:    time of the last measure
    """

    def __init__(self):
        self.baseline = time.time()
        self.baseline_global = time.time()


    def get_time(self):
        """
            It gives the time passed since the last measure. It restart everytime it is asked.

            Returns:
                time as string rounded at 2
        """

        seconds = time.time() - self.baseline

        # reset time
        self.baseline = time.time()

        return seconds


    def get_global_time(self):
        """
            It gives the time passed since the first measure.

            Returns:
                time as string rounded at 2
        """

        return time.time() - self.baseline_global


def wait_until(final_time):
    """
        Function waits a number of seconds
        args: Final timestamp
        returns: None
    """

    while True:
        mtime = (final_time - datetime.now()).total_seconds()
        if mtime <= 0:
            break
        print("Waiting {} seconds".format(mtime))
        time.sleep(mtime)


def get_random_if_greater_than_ten():
    """
        lorem ipsum
    """

    mrandom = random.random()

    if random > 10:
        return mrandom
    return None
