from game_object import GameObject
from visual.visual import VisualComponents
from events.keyboard_event import KeyBoardEvent
from events.event import EventServer
from events.game_start_event import GameStartEvent
import pygame

class Button(GameObject):
    def __init__(self, visual: VisualComponents):
        super().__init__()
        EventServer.bind(self.on_key_pressed, KeyBoardEvent)
        self.visual = visual
        font = pygame.font.Font("font.ttf", 40)
        self.text = font.render("Press enter to play", True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (visual.size[0] * 0.5, 
                                 visual.size[1] * 0.5)
    
    def on_key_pressed(self, event: KeyBoardEvent):
        if event.key == pygame.K_SPACE:
            EventServer.pool(GameStartEvent())

    def update(self):
        self.visual.win.screen.blit(self.text, self.text_rect)