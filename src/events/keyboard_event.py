from events.event import Event

class KeyBoardEvent(Event):
    def __init__(self, key):
        self.key = key