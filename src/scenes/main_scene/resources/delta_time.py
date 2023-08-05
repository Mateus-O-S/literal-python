from time import time

class DeltaTime:
    __start = 0
    __end = 0

    @staticmethod
    def set_start():
        DeltaTime.__start = time()
    
    @staticmethod
    def set_end():
        DeltaTime.__end = time()
    
    @staticmethod
    def delta_time():
        delta = DeltaTime.__end - DeltaTime.__start
        if delta >= 0:
            return delta
        return 0