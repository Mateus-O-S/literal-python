from events.event import Event

class TimeEvent(Event):
    def __init__(self, time):
        self.time = time