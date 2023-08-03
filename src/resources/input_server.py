from game_object import GameObject
from events.event import EventServer
from events.window_event import WindowEvent
from events.keyboard_event import KeyBoardEvent
import pygame

class InputServer(GameObject):
    def __init__(self):
        super().__init__()
    
    def setup(self):
        EventServer.bind(self.check_input, WindowEvent)
    
    def check_input(self, event: WindowEvent):
        if event.pygame_event.type == pygame.KEYDOWN:
            EventServer.pool(KeyBoardEvent(event.pygame_event.key))