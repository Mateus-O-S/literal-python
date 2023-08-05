from game_object import GameObject
from events.event import EventServer
from events.time_event import TimeEvent
import time

class Timer(GameObject):
    def __init__(self):
        super().__init__()
        self.start = time.time()
    
    def update(self):
        EventServer.pool(TimeEvent(self.get_time()))

    def get_time(self):
        return time.time() - self.start