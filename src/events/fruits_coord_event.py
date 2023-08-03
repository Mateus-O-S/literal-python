from events.event import Event

class FruitCoordEvent(Event):
    def __init__(self, fruits):
        self.fruits = fruits