from events.event import Event

class SnakeSizeEvent(Event):
    def __init__(self, size):
        self.size = size