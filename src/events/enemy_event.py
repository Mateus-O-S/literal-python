from events.event import Event

class EnemyEvent(Event):
    def __init__(self, body):
        self.body = body