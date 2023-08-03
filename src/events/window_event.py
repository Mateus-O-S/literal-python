from events.event import Event

class WindowEvent(Event):
    def __init__(self, pygame_event):
        self.pygame_event = pygame_event