from events.event import Event

class DestroyEnemyPartEvent(Event):
    def __init__(self, part) -> None:
        self.part = part