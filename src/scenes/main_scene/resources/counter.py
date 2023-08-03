from time import time

class Counter:
    __start = 0
    __end = 0

    @staticmethod
    def set_start():
        Counter.__start = time()
    
    @staticmethod
    def set_end():
        Counter.__end = time()
    
    @staticmethod
    def delta_time():
        delta = Counter.__end - Counter.__start
        if delta >= 0:
            return delta
        return 0