from game_object import GameObject
from events.event import EventServer
from events.window_event import WindowEvent
import pygame

class WindowClosingHandler(GameObject):
    def __init__(self):
        super().__init__()
    
    def setup(self):
        EventServer.bind(self.handle_events, WindowEvent)
    
    def handle_events(self, event):
        if event.pygame_event.type == pygame.WINDOWCLOSE:
                exit(0)