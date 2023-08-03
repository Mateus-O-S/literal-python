import pygame

class Drawer:
    def __init__(self, scale: int, surface: pygame.surface.Surface):
        self.surface = surface
        self.scale = scale

    def draw_pixel(self, x, y, color):
        rect = (x * self.scale, y * self.scale, self.scale, self.scale)
        pygame.draw.rect(self.surface, color, rect)