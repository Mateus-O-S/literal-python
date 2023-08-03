import pygame
from events.window_event import WindowEvent
from events.event import EventServer

class Window:
    def __init__(self, caption='', mode=(0, 0)):
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(mode)

    def update(self):
        pygame.display.update()
        for e in pygame.event.get():
            EventServer.pool(WindowEvent(e))