from game_object import GameObject
from visual.visual import VisualComponents
import pygame

class Title(GameObject):
    def __init__(self, visual: VisualComponents):
        super().__init__()
        self.visual = visual
        font = pygame.font.Font("font.ttf", 64)
        self.text = font.render("Game Over", True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (visual.size[0] * 0.5, 
                                 visual.size[1] * 0.2)
        
    def update(self):
        self.visual.win.screen.blit(self.text, self.text_rect)